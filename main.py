from run_query import run_query

# define the query
query = """
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