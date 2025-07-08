def printing_model(unprinted_designs,completed_models):
    """Takes a 2 lists of designs and prints the first and moves its items to the second """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)