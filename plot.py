import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

def plot_graph():
    # collect data from db
    con = create_engine(f"mysql+mysqlconnector://root:@localhost/",echo=False)
    query = """SELECT f_timestamp,f_value
                FROM db_termal.tb_raw_history"""
    df = pd.read_sql(query, con)
    df['f_timestamp'] = df['f_timestamp'].apply(lambda x: pd.Timestamp(x).strftime('%H:%M:%S'))
    df = df.set_index("f_timestamp")
    
    # plotting
    ax = df.plot()

    ax.grid(which ='minor', alpha = 0.2)
    ax.grid(which ='major', alpha = 0.5)

    ax.legend().set_visible(False)
    plt.xticks(rotation = 30)
    plt.tight_layout()
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.title("Suhu Udara")
    plt.tight_layout()
    
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
    
