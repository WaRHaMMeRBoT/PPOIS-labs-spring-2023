import argparse
import Db_Utility
import Simulation

def cli():
    parser = argparse.ArgumentParser(description='RailwayModelSimulation CLI')
    parser.add_argument('--auto', action='store_true', help='Enable auto mode')
    parser.add_argument('-iterations', type=int, default=1, help='Number of iterations (default: 1)')
    parser.add_argument('--graphdb', action='store_true', help='Display the graph')
    parser.add_argument('--traindb', action='store_true', help='Display the train db')
    parser.add_argument('-add', nargs='+', type=int, help='Add elm (1 value for node,3 values for edge) to the graph \
                        or data to the train db (3 values: train_number, locomotive_speed, trainCar_value)')
    parser.add_argument('-rm',nargs='+',type=int,help='Remove elm (1 value for node, 3 values for edge) from graph \
                        or data from the train db (1 value: train_number)')
    args = parser.parse_args()

    def add_elm_graph(elm):
        Db_Utility.add_to_graph(elm)

    def remove_elm_graph(elm):
        Db_Utility.del_from_graph(elm)
        
    def add_train_db(elm):
        Db_Utility.add_to_trains(elm)

    def remove_train_db(elm):
        Db_Utility.del_from_trains(elm)

    def start_simulation(iterations):
        Simulation.Simulation(iterations)

    if args.graphdb:
        graph=Db_Utility.load_graph_data()
        print(graph)
        
    if args.add and args.graphdb:
        add_elm_graph(args.add)
        print(f'Added elm: {args.add} \n')
        graph=Db_Utility.load_graph_data()
        print(graph)

    if args.rm and args.graphdb:
        remove_elm_graph(args.rm)
        print(f'Removed elm: {args.rm} \n')
        graph=Db_Utility.load_graph_data()
        print(graph)

    if args.traindb:
        trains = Db_Utility.load_train_data()
        for train in trains: 
            print(train)

    if args.add and args.traindb:
        add_train_db(args.add)
        print(f'Added train: {args.add} \n')
        trains = Db_Utility.load_train_data()
        for train in trains: 
            print(train)
    
    if args.rm and args.traindb:
        remove_train_db(args.rm)
        print(f'Removed train: {args.rm} \n')

    if args.auto:
        print('Auto modeling enabled\n')

    if args.auto and args.iterations:
        start_simulation(args.iterations)

cli()
