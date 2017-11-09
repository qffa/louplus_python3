import pandas as pd

def analysis(file, user_id):
    df = pd.read_json(file)
    times = df[df['user_id'] == user_id]['minutes'].count()
    minutes = df[df['user_id'] == user_id]['minutes'].sum()


    return times, minutes
