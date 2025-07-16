from network_config import select_network_mode
from routing import run_distance_vector_simulation

if __name__ == "__main__":
    # Selezione della topologia di rete da utilizzare
    network_topology = select_network_mode()
    # Avvio della simulazione del protocollo Distance Vector
    run_distance_vector_simulation(network_topology)