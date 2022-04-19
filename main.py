from run_query import run_query
import pandas as pd

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
run_query(query)