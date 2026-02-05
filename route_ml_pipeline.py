import pandas as pd
import numpy as np
import networkx as nx
from topsis import run_topsis


# ---------------------------
# Candidate Route Generation
# ---------------------------
def generate_candidate_routes(df, source, destination, graph=None):

    # Graph feasibility check
    if graph is not None:
        try:
            nx.shortest_path(graph, source, destination)
        except:
            return pd.DataFrame()

    # Dataset filtering
    candidates = df[
        (df["source"].str.lower().str.strip() == source.lower().strip()) &
        (df["destination"].str.lower().str.strip() == destination.lower().strip())
    ].copy()

    return candidates


# ---------------------------
# Context Modifiers
# ---------------------------
def apply_context_modifiers(route_df, context=None):

    df_mod = route_df.copy()

    if context is None:
        return df_mod

    if context == "night":
        df_mod["safety"] = df_mod["safety"] * 1.15

    if context == "rain":
        df_mod["road_quality"] = df_mod["road_quality"] * 1.10

    if context == "rush_hour":
        df_mod["traffic"] = df_mod["traffic"] * 1.20

    return df_mod


# ---------------------------
# TOPSIS Ranking Wrapper
# ---------------------------
def rank_routes_topsis(route_df, weights_dict):

    working_df = route_df.copy()

    weights = [
        weights_dict["safety"],
        weights_dict["time"],
        weights_dict["distance"],
        weights_dict["traffic"],
        weights_dict["road_quality"]
    ]

    working_df = working_df.rename(columns={
        "route_name": "Route",
        "safety": "Safety (1-5)",
        "distance": "Distance (km)",
        "time": "Time (min)",
        "traffic": "Traffic (1-10)",
        "road_quality": "Road Quality (1-5)"
    })

    result_df = run_topsis(working_df, weights)

    return result_df


# ---------------------------
# Master Recommendation Pipeline
# ---------------------------
def recommend_route(
    df,
    source,
    destination,
    weights_dict,
    context=None,
    graph=None
):

    if graph is None:
        print("Warning: No graph provided — using dataset-only filtering")

    candidates = generate_candidate_routes(
        df, source, destination, graph
    )

    if len(candidates) == 0:
        return None

    candidates = apply_context_modifiers(
        candidates, context
    )

    ranked = rank_routes_topsis(
        candidates, weights_dict
    )

    return ranked
