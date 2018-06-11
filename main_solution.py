# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:57:52 2018

@author: AyodejiAkiwowo
"""

import data
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2

data = DataProblem()

routing = pywrapcp.RoutingModel(data.num_locations, data.num_vehicles, data.depot)

distance_evaluator = CreateDistanceEvaluator(data).distance_evaluator
routing.SetArcCostEvaluatorOfAllVehicles(distance_evaluator)

demand_evaluator = CreateDemandEvaluator(data).demand_evaluator
add_capacity_constraints(routing, data, demand_evaluator)

search_parameters = pywrapcp.RoutingModel.DefaultSearchParameters()
search_parameters.first_solution_strategy = (routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

assignment = routing.SolveWithParameters(search_parameters)

printer = ConsolePrinter(data, routing, assignment)
printer.print()