import base64
from unittest import mock
import copy

from pyband.client import Client
from pyband.auth import Auth

from google.protobuf.timestamp_pb2 import Timestamp

from pyband.proto.oracle.v1.query_pb2 import QueryRequestResponse
from pyband.proto.oracle.v1.oracle_pb2 import Request, Report, Result, IBCChannel
from pyband.proto.cosmos.base.tendermint.v1beta1.query_pb2 import GetLatestBlockResponse
from pyband.proto.tendermint.types.types_pb2 import BlockID
from pyband.proto.tendermint.types.types_pb2 import Header
from pyband.proto.tendermint.types.block_pb2 import Block


VALIDATOR_TEST = "bandvaloper1p40yh3zkmhcv0ecqp3mcazy83sa57rgjde6wec"


BlOCK_TEST = GetLatestBlockResponse(
    block_id=BlockID(
        hash=bytes.fromhex("391E99908373F8590C928E0619956DA3D87EB654445DA4F25A185C9718561D53"),
    ),
    block=Block(
        header=Header(
            chain_id="bandchain",
            height=136639,
            time=Timestamp().FromJsonString("2020-11-05T09:15:18.445494105Z"),
            last_commit_hash=bytes.fromhex("17B2CE4ABA910E85847537F1323DB95C9F16C20C60E9B9BBB04C633C3125BD92"),
            data_hash=bytes.fromhex("EFE5E3F549554FEE8EB9B393740C250D74580427A96A175ABB105806039CFFE2"),
            validators_hash=bytes.fromhex("E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151"),
            next_validators_hash=bytes.fromhex("E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151"),
            consensus_hash=bytes.fromhex("0EAA6F4F4B8BD1CC222D93BBD391D07F074DE6BE5A52C6964875BB355B7D0B45"),
            app_hash=bytes.fromhex("6E2B1ECE9D912D86C25182E8B7419583ABCE978BFC66DC2556BB0D06A8D528EF"),
            last_results_hash=bytes.fromhex(""),
            evidence_hash=bytes.fromhex(""),
            proposer_address=bytes.fromhex("BDB6A0728C8DFE2124536F16F2BA428FE767A8F9"),
        )
    ),
)

BlOCK_WRONG_TEST = GetLatestBlockResponse(
    block_id=BlockID(
        hash=bytes.fromhex("391E99908373F8590C928E0619956DA3D87EB654445DA4F25A185C9718561D53"),
    ),
    block=Block(
        header=Header(
            chain_id="bandchain",
            height=136730,
            time=Timestamp().FromJsonString("2020-11-05T09:15:18.445494105Z"),
            last_commit_hash=bytes.fromhex("17B2CE4ABA910E85847537F1323DB95C9F16C20C60E9B9BBB04C633C3125BD92"),
            data_hash=bytes.fromhex("EFE5E3F549554FEE8EB9B393740C250D74580427A96A175ABB105806039CFFE2"),
            validators_hash=bytes.fromhex("E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151"),
            next_validators_hash=bytes.fromhex("E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151"),
            consensus_hash=bytes.fromhex("0EAA6F4F4B8BD1CC222D93BBD391D07F074DE6BE5A52C6964875BB355B7D0B45"),
            app_hash=bytes.fromhex("6E2B1ECE9D912D86C25182E8B7419583ABCE978BFC66DC2556BB0D06A8D528EF"),
            last_results_hash=bytes.fromhex(""),
            evidence_hash=bytes.fromhex(""),
            proposer_address=bytes.fromhex("BDB6A0728C8DFE2124536F16F2BA428FE767A8F9"),
        )
    ),
)


REQUEST_TEST = QueryRequestResponse(
    request=Request(
        oracle_script_id=1,
        calldata=base64.b64decode("AAAABFVTRFQAAAADQ05ZAAAAAAAPQkA="),
        requested_validators=[
            "bandvaloper1yplk6n4wmeaarxp966gukpxupg3jqfcqkh32mw",
            "bandvaloper1v38hewjc0865dm4t89v5efh9rmum5rmrm7evg4",
            "bandvaloper1alzj765pzuhtjkmslme4fdpeakc0036xnyjltn",
            "bandvaloper1yyv5jkqaukq0ajqn7vhkyhpff7h6e99j3gv0tr",
            "bandvaloper1p40yh3zkmhcv0ecqp3mcazy83sa57rgjde6wec",
        ],
        min_count=3,
        request_height=136629,
        client_id="test",
        raw_requests=[],
        ibc_channel=IBCChannel(),
        execute_gas=40000,
    ),
    reports=[
        Report(
            validator="bandvaloper1yplk6n4wmeaarxp966gukpxupg3jqfcqkh32mw", raw_reports=[], in_before_resolve=False
        ),
        Report(validator="bandvaloper1yyv5jkqaukq0ajqn7vhkyhpff7h6e99j3gv0tr", raw_reports=[], in_before_resolve=True),
    ],
    result=Result(
        oracle_script_id=1,
        ask_count=5,
        min_count=3,
        request_time=1596950963,
        resolve_time=1596950966,
        resolve_status="RESOLVE_STATUS_SUCCESS",
        request_id=1,
        ans_count=1,
        client_id="test",
        result=base64.b64decode("AAAABFVTRFQAAAADQ05ZAAAAAAAPQkA="),
        calldata=base64.b64decode("AAAAAABqbB0="),
    ),
)


def test_get_msg_sign_bytes():
    assert Auth.get_msg_sign_bytes("bandchain", VALIDATOR_TEST, "1", "1") == bytes.fromhex(
        "7b22636861696e5f6964223a2262616e64636861696e222c2265787465726e616c5f6964223a2231222c22726571756573745f6964223a2231222c2276616c696461746f72223a2262616e6476616c6f706572317034307968337a6b6d6863763065637170336d63617a7938337361353772676a646536776563227d"
    )


def test_verify_verification_message():
    assert (
        Auth.verify_verification_message_signature(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            base64.b64decode(
                "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ=="
            ),
        )
        == True
    )


@mock.patch("pyband.client.Client")
def test_verify(mock_client):
    auth = Auth(mock_client)
    # Fail signature verification
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "2",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == False
    )

    # Wrong chain id
    mock_client.get_chain_id.return_value = "fake_id"
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == False
    )

    mock_client.get_chain_id.return_value = "bandchain"

    # Unauthorized reporter
    mock_client.get_reporters.return_value = [
        "band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        "band1ath4dk8e4fwqs5qmp3nnxspar5q0arrtpxy8lx",
    ]
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == False
    )
    mock_client.get_reporters.return_value = ["band1wmvh4uzemujfap5graugzckeazr39uy6lesd0g"]

    # Expired request
    mock_client.get_request_by_id.return_value = REQUEST_TEST
    mock_client.get_latest_block.return_value = BlOCK_WRONG_TEST
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == False
    )
    mock_client.get_latest_block.return_value = BlOCK_TEST

    request = copy.deepcopy(REQUEST_TEST)
    request.request.requested_validators[:] = request.request.requested_validators[:-1]
    mock_client.get_request_by_id.return_value = request
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == False
    )

    # Must return false if validator already reported data.
    request = copy.deepcopy(REQUEST_TEST)
    del request.reports[:]
    request.reports.extend([Report(validator=VALIDATOR_TEST, raw_reports=[], in_before_resolve=True)])
    mock_client.get_request_by_id.return_value = request
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == False
    )

    mock_client.get_request_by_id.return_value = REQUEST_TEST
    assert (
        auth.verify(
            "bandchain",
            VALIDATOR_TEST,
            "1",
            "1",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
            "IsgagGxxSVHOPyzProTYBW9sFNMjLGkuDm+JvLgBH8Ux6GMpj3p6e5YGY8KRVWV3fdYWm/UBZdpVqsMbnpV6PQ==",
        )
        == True
    )


@mock.patch("pyband.client.Client")
def test_verify_chain_id(mock_client):
    auth = Auth(mock_client)

    mock_client.get_chain_id.return_value = "bandchain"
    assert auth.verify_chain_id("bandchain") == True
    assert auth.verify_chain_id("band-testnet") == False


@mock.patch("pyband.client.Client")
def test_is_reporter(mock_client):
    auth = Auth(mock_client)

    mock_client.get_reporters.return_value = [
        "band13eznuehmqzd3r84fkxu8wklxl22r2qfmtlth8c",
        "band1ath4dk8e4fwqs5qmp3nnxspar5q0arrtpxy8lx",
    ]
    assert (
        auth.is_reporter(
            "mock_validator",
            "bandpub1addwnpepqdg7nrsmuztj2re07svgcz4vuzn3de56nykdwlualepkk05txs5q6mw8s9v",
        )
        == True
    )
    assert (
        auth.is_reporter(
            "mock_validator",
            "bandpub1addwnpepqgugvxy0ueqwfmlzh2ta5at2lumcy4wpzzjs4hjz8j44lrdcryqs66wh3rp",
        )
        == False
    )


@mock.patch("pyband.client.Client")
def test_verify_non_expired_request(mock_client):
    auth = Auth(mock_client)

    mock_client.get_latest_block.return_value = BlOCK_TEST
    assert auth.verify_non_expired_request(REQUEST_TEST.request) == True

    mock_client.get_latest_block.return_value = BlOCK_WRONG_TEST
    assert auth.verify_non_expired_request(REQUEST_TEST.request) == False


def test_verify_requested_validator():
    request = REQUEST_TEST.request
    auth = Auth(Client("xxx"))
    assert auth.verify_requested_validator(request, "bandvaloper1yplk6n4wmeaarxp966gukpxupg3jqfcqkh32mw") == True
    assert auth.verify_requested_validator(request, "bandvaloper1trx2cm6vm9v63grg9uhmk7sy233zve4q25rgre") == False
    assert auth.verify_requested_validator(request, "bandvaloper1yyv5jkqaukq0ajqn7vhkyhpff7h6e99j3gv0tr") == True


def test_verify_unsubmitted_report():
    reports = REQUEST_TEST.reports
    auth = Auth(Client("xxx"))
    assert auth.verify_unsubmitted_report(reports, "bandvaloper1yplk6n4wmeaarxp966gukpxupg3jqfcqkh32mw") == False
    assert auth.verify_unsubmitted_report(reports, "bandvaloper1alzj765pzuhtjkmslme4fdpeakc0036xnyjltn") == True
