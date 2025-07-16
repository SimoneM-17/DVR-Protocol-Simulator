sample_topology = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 3, 'D': 1},
    'C': {'A': 5, 'B': 3, 'E': 7},
    'D': {'B': 1, 'E': 4, 'F': 8},
    'E': {'C': 7, 'D': 4, 'G': 2},
    'F': {'D': 8, 'G': 6, 'H': 3},
    'G': {'E': 2, 'F': 6, 'H': 1},
    'H': {'F': 3, 'G': 1}
}

# Acquisizione della configurazione di rete tramite input utente
# Consente la definizione manuale di una topologia di rete
# specificando nodi, collegamenti diretti e relativi costi
def build_custom_topology():
    """
    Permette all'utente di configurare manualmente una topologia di rete
    definendo nodi, connessioni e i relativi costi di collegamento.
    
    Returns:
        Dizionario rappresentante la topologia di rete configurata
    """
    topology = {}
    print("Configurazione manuale della topologia di rete...")

    # Richiesta del numero totale di nodi da configurare
    total_nodes = int(input("Inserire il numero totale di nodi nella rete: "))

    # Configurazione iterativa di ogni nodo e dei suoi collegamenti
    for node_index in range(total_nodes):
        node_identifier = input(f"Inserisci l'identificatore del nodo {node_index + 1}: ")
        topology[node_identifier] = {}
        print(f"Inserisci i collegamenti diretti per il nodo {node_identifier}:")

        # Aggiunta iterativa dei collegamenti (nodo destinazione e costo)
        while True:
            connection_input = input(f"Collegamenti per {node_identifier} (formato: NodoDestinazioneXCosto) oppure 'fine' per terminare: ")
            if connection_input == "fine":
                break

            try:
                # Parsing dell'input per estrarre nodo destinazione e costo del collegamento
                destination_node, link_cost = connection_input.split(',')
                link_cost = int(link_cost)
                topology[node_identifier][destination_node] = link_cost
                # Creazione del collegamento bidirezionale (grafo non orientato)
                if destination_node not in topology:
                    topology[destination_node] = {}
                topology[destination_node][node_identifier] = link_cost
            except ValueError:
                print("Formato del collegamento non valido, riprova (esempio: 'B,1').")
    
    return topology

# Visualizzazione della struttura di rete in formato comprensibile
def display_network_structure(topology):
    """
    Stampa la struttura della rete in un formato leggibile e organizzato.
    
    Args:
        topology: Dizionario che rappresenta la topologia di rete
    """
    print("\nStruttura della rete corrente:")
    for node_name, connections in topology.items():
        print(f"{node_name} -> {connections}")

# Selezione della modalità di configurazione della rete
# Offre all'utente la possibilità di scegliere tra una topologia
# predefinita o la configurazione di una topologia personalizzata
def select_network_mode():
    """
    Permette all'utente di scegliere tra topologia predefinita o personalizzata.
    
    Returns:
        Dizionario rappresentante la topologia di rete selezionata
    """
    print("Seleziona la modalità di configurazione della rete:")
    user_choice = input("Scrivi 'predefinita' per la topologia di esempio o 'personalizzata' per configurarne una: ").strip().lower()

    if user_choice == 'predefinita':
        print("\nUtilizzo della topologia di esempio:")
        display_network_structure(sample_topology)
        return sample_topology
    elif user_choice == 'personalizzata':
        return build_custom_topology()
    else:
        print("Selezione non riconosciuta, utilizzo della topologia predefinita.")
        display_network_structure(sample_topology)
        return sample_topology