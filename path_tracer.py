from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

adjacency = {
    1: [2],
    2: [1, 3],
    3: [2]
}

host_locations = {}

def get_path(src, dst):
    if src == dst:
        return [src]
    visited = []
    queue = [[src]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            visited.append(node)
            if node in adjacency:
                for neighbor in adjacency[node]:
                    new_path = path + [neighbor]
                    if neighbor == dst:
                        return new_path
                    queue.append(new_path)
    return None

class PathTracer(object):
    def __init__(self):
        core.openflow.addListeners(self)
        log.info("PathTracer Started!! Waiting for switches...")

    def _handle_ConnectionUp(self, event):
        switch_id = event.dpid
        log.info("Switch %s connected!!", switch_id)

    def _handle_PacketIn(self, event):
        packet = event.parsed
        switch_id = event.dpid
        in_port = event.port
        if not packet.parsed:
            return
        src_mac = str(packet.src)
        dst_mac = str(packet.dst)
        host_locations[src_mac] = (switch_id, in_port)
        log.info("Host %s is at Switch %s Port %s", src_mac, switch_id, in_port)
        if dst_mac in host_locations:
            dst_switch = host_locations[dst_mac][0]
            path = get_path(switch_id, dst_switch)
            if path:
                log.info("=================================")
                log.info("PATH FOUND: %s --> %s", src_mac, dst_mac)
                log.info("Route: %s", " --> ".join("Switch "+str(s) for s in path))
                log.info("=================================")
            else:
                log.info("No path found between %s and %s", src_mac, dst_mac)
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

def launch():
    log.info("Starting Path Tracer Tool!!")
    core.registerNew(PathTracer)