from run_query import run_query
import pandas as pd


if __name__ == "__main__":
    # define the query
    query: str = """
    {
          listUsers{
            items{
              name
              availability
              email
              createdAt
            }
          }
        }
        """
    response = run_query(query)
    print(response)
