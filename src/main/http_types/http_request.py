from typing import Dict

class HttpRequest:

  def __init__(
    self,
    header: Dict = None,
    body: Dict = None,
    query_params = None,
    path_params = None,
    url: str = None,
    ipv4: str = None,
    toke_information: Dict = None
  ):
    self.header = header
    self.body = body
    self.query_params = query_params
    self.path_params = path_params
    self.url - url
    self.ipv4 = ipv4
    self.token_information - toke_information

  def __repr__(self):
    return(
      f"HttpRequest (header={self.header}, body={self.body}, query={self.query_params})"
    )