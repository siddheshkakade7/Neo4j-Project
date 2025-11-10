
import pandas as pd
from connect import get_driver

def run_query_to_csv(query: str, output_path: str):
    driver = get_driver()
    with driver.session() as session:
        result = session.run(query)
        records = [record.data() for record in result]
        if records:
            df = pd.DataFrame(records)
            df.to_csv(output_path, index=False)
        else:
            print("No results to save.")

if __name__ == "__main__":
    cypher_query = "MATCH (n) RETURN n LIMIT 10"  # Example query
    output_file = "output/query_results.csv"
    run_query_to_csv(cypher_query, output_file)
    print(f"Results saved to {output_file}")
