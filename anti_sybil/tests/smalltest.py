# test effect of running sybil rank on graph of groups instead of graph of individuals

import algorithms
import copy
from utils import *

OUTPUT_FOLDER = './outputs/smalltest/'

algorithm_options = {
    'min_degree': 5,
    'accumulative': False,
    'weaken_under_min': True,
    'nonlinear_distribution': True,
    'group_edge_weight': 2
}
main_graph_params = {
    'num_groups': 14,
    'num_seed_groups': 2,
    'min_group_nodes': 3,
    'max_group_nodes': 20,
    'max_known_ratio': 1,
    'avg_known_ratio': .5,
    'min_known_ratio': .2,
    'num_seed_nodes': 20,
    'num_attacker_to_num_honest': 0,
    'num_sybil_to_num_attacker': 1,
    'sybil_to_attackers_con': .1,
    'num_joint_node': 120,
    'num_inter_group_con': 120
}


def test(graph_params):
    graph = graphs.generators.group_based.generate(graph_params)
    group_graph = algorithms.SybilGroupRank(graph, algorithm_options).rank()
    output2 = generate_output(graph)

    return [output2]


if __name__ == '__main__':
    outputs = []
    graph_params = copy.copy(main_graph_params)
    outputs.extend(test(graph_params))

    # graph_params = copy.copy(main_graph_params)
    # graph_params['sybil_to_attackers_con'] = .7
    # outputs.extend(test(graph_params))
    #
    # graph_params = copy.copy(main_graph_params)
    # graph_params['num_groups'] = 30
    # graph_params['min_group_nodes'] = 30
    # graph_params['max_group_nodes'] = 70
    # outputs.extend(test(graph_params))
    #
    # graph_params = copy.copy(main_graph_params)
    # graph_params['num_seed_groups'] = 15
    # graph_params['num_seed_nodes'] = 150
    # outputs.extend(test(graph_params))
    #
    # graph_params = copy.copy(main_graph_params)
    # graph_params['num_joint_node'] = 2000
    # graph_params['num_inter_group_con'] = 5000
    # outputs.extend(test(graph_params))
    #
    # graph_params = copy.copy(main_graph_params)
    # graph_params['num_joint_node'] = 100
    # outputs.extend(test(graph_params))
    #
    # graph_params = copy.copy(main_graph_params)
    # graph_params['num_inter_group_con'] = 100
    # outputs.extend(test(graph_params))

    write_output_file(outputs, os.path.join(OUTPUT_FOLDER, 'result.csv'))
