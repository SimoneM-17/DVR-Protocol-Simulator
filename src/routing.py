import copy
import time

# Creazione delle tabelle di instradamento iniziali seguendo questa logica:
# - Costo verso il nodo corrente: 0
# - Costo verso i nodi adiacenti: peso del collegamento diretto
# - Costo verso tutti gli altri nodi: valore infinito
def create_initial_tables(topology):
    """
    Inizializza le tabelle di instradamento per tutti i nodi della rete.
    
    Args:
        topology: Dizionario che rappresenta la topologia di rete
        
    Returns:
        Dizionario contenente le tabelle di instradamento iniziali
    """
    distance_tables = {}
    for current_node in topology:
        # Imposta tutte le distanze a infinito come valore iniziale
        distance_tables[current_node] = {dest: float('inf') for dest in topology}
        distance_tables[current_node][current_node] = 0  # Distanza verso sé stesso è sempre 0
        for adjacent_node, link_cost in topology[current_node].items():
            distance_tables[current_node][adjacent_node] = link_cost  # Costo verso nodi adiacenti
    return distance_tables

# Procedura di aggiornamento delle tabelle di instradamento
# Applica l'algoritmo Distance Vector utilizzando le informazioni
# ricevute dai nodi vicini per calcolare i percorsi ottimali
def refresh_distance_tables(topology, distance_tables):
    """
    Aggiorna le tabelle di instradamento basandosi sulle informazioni dei nodi vicini.
    
    Args:
        topology: Topologia della rete
        distance_tables: Tabelle di instradamento attuali
        
    Returns:
        Tupla contenente le nuove tabelle e un flag di cambiamento
    """
    has_changed = False  # Indicatore per rilevare modifiche
    updated_tables = copy.deepcopy(distance_tables)  # Copia profonda delle tabelle correnti

    for current_node in topology:  # Scorre tutti i nodi
        for adjacent_node, direct_cost in topology[current_node].items():  # Esamina ogni nodo vicino
            for target_node, neighbor_distance in distance_tables[adjacent_node].items():
                # Calcola il costo del percorso attraverso il nodo vicino
                if distance_tables[current_node][adjacent_node] != float('inf'):
                    alternative_path_cost = distance_tables[current_node][adjacent_node] + neighbor_distance
                    # Aggiorna se il nuovo percorso è più conveniente
                    if alternative_path_cost < updated_tables[current_node][target_node]:
                        updated_tables[current_node][target_node] = alternative_path_cost
                        has_changed = True  # Registra il cambiamento avvenuto

    return updated_tables, has_changed

# Esecuzione della simulazione del protocollo Distance Vector Routing
# Esegue iterativamente l'algoritmo fino al raggiungimento della convergenza
# o al superamento del limite massimo di iterazioni consentite
def run_distance_vector_simulation(topology, max_cycles=100):
    """
    Simula il protocollo Distance Vector Routing fino alla convergenza.
    
    Args:
        topology: Topologia della rete da simulare
        max_cycles: Numero massimo di iterazioni consentite
        
    Returns:
        Tabelle di instradamento finali
    """
    # Crea le tabelle di instradamento iniziali
    distance_tables = create_initial_tables(topology)
    print("\nCreazione delle tabelle di instradamento iniziali:")
    display_routing_tables(distance_tables)

    # Ciclo di aggiornamento iterativo delle tabelle
    for cycle_number in range(max_cycles):
        print(f"\nCiclo di aggiornamento {cycle_number + 1}:")
        new_distance_tables, has_updates = refresh_distance_tables(topology, distance_tables)
        display_routing_tables(new_distance_tables)

        if not has_updates:  # Se non ci sono modifiche, la convergenza è stata raggiunta
            print("\nStato di convergenza raggiunto con successo")
            print("\nTabelle di instradamento finali:")
            display_routing_tables(new_distance_tables)
            break

        distance_tables = new_distance_tables  # Prepara le tabelle per il prossimo ciclo
        
        time.sleep(1)  # Pausa di 1 secondo tra le iterazioni
    else:
        print("\nRaggiunto il limite massimo di iterazioni senza convergenza.")

    return distance_tables

# Visualizzazione delle tabelle di instradamento per ciascun nodo
def display_routing_tables(distance_tables):
    """
    Stampa in formato leggibile le tabelle di instradamento di tutti i nodi.
    
    Args:
        distance_tables: Dizionario contenente le tabelle di instradamento
    """
    for node_name, routing_table in distance_tables.items():
        print(f"Tabella del nodo {node_name}: {routing_table}")