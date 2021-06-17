import pytest

from google.protobuf import any_pb2
from pyband.proto.oracle.v1.query_pb2 import QueryDataSourceRequest, QueryDataSourceResponse
from pyband.proto.oracle.v1.oracle_pb2 import DataSource
from pyband.proto.oracle.v1.query_pb2_grpc import QueryServicer as OracleServicerBase
from pyband.proto.cosmos.auth.v1beta1.query_pb2_grpc import QueryServicer as AuthServicerBase
from pyband.proto.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from pyband.proto.cosmos.auth.v1beta1.query_pb2 import QueryAccountRequest, QueryAccountResponse


class OracleServicer(OracleServicerBase):
    def DataSource(self, request: QueryDataSourceRequest, context) -> QueryDataSourceResponse:
        print(type(request))
        if request.data_source_id == 1:
            return QueryDataSourceResponse(data_source=DataSource(name="Blue"))
        return QueryDataSourceResponse(data_source=DataSource(name="Blue2"))


class AuthServicer(AuthServicerBase):
    def Account(self, request, context):
        acc = BaseAccount(account_number=3)
        any = any_pb2.Any()
        any.Pack(acc)
        return QueryAccountResponse(account=any)


# @pytest.fixture(scope="module")
# def grpc_add_to_server():
#     from pyband.proto.oracle.v1.query_pb2_grpc import add_QueryServicer_to_server

#     return add_QueryServicer_to_server


# @pytest.fixture(scope="module")
# def grpc_servicer():
#     return OracleServicer()


# @pytest.fixture(scope="module")
# def pyband_client(grpc_channel):

#     from pyband.client import Client

#     from pyband.proto.oracle.v1.query_pb2_grpc import QueryStub as OracleStub

#     client = Client("mock")
#     client.stubOracle = OracleStub(grpc_channel)
#     return client


@pytest.fixture(scope="module")
def pyband_client(_grpc_server, grpc_addr):

    from pyband.proto.oracle.v1.query_pb2_grpc import add_QueryServicer_to_server as add_oracle
    from pyband.proto.cosmos.auth.v1beta1.query_pb2_grpc import add_QueryServicer_to_server as add_auth

    add_oracle(OracleServicer(), _grpc_server)
    add_auth(AuthServicer(), _grpc_server)
    _grpc_server.add_insecure_port(grpc_addr)
    _grpc_server.start()

    from pyband.client import Client

    yield Client(grpc_addr)
    _grpc_server.stop(grace=None)


def test_some(pyband_client):
    data_source = pyband_client.get_data_source(1)

    assert data_source.name == "Blue"

    data_source = pyband_client.get_data_source(2)

    assert data_source.name == "Blue2"

    account = pyband_client.get_account("xxx")

    assert account.account_number == 3
