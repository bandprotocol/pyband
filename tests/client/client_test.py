import pytest
import grpc

# Servicers
from pyband.proto.oracle.v1.query_pb2_grpc import QueryServicer as OracleServicerBase
from pyband.proto.cosmos.auth.v1beta1.query_pb2_grpc import QueryServicer as AuthServicerBase
from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceServicer as CosmosTxServicerBase
from pyband.proto.cosmos.base.tendermint.v1beta1.query_pb2_grpc import ServiceServicer as TendermintServicerBase

# Types
from pyband.proto.oracle.v1.oracle_pb2 import DataSource, OracleScript
from pyband.proto.cosmos.auth.v1beta1.auth_pb2 import BaseAccount
from pyband.proto.cosmos.auth.v1beta1.query_pb2 import QueryAccountResponse
from pyband.proto.oracle.v1.query_pb2 import (
    QueryDataSourceRequest,
    QueryDataSourceResponse,
    QueryOracleScriptResponse,
    QueryRequestRequest,
    QueryRequestResponse,
    QueryReportersRequest,
    QueryReportersResponse,
    QueryRequestPriceRequest,
    QueryRequestPriceResponse,
    QueryRequestSearchRequest,
    QueryRequestSearchResponse,
)

from pyband.proto.oracle.v1.oracle_pb2 import Result, Report, Request, RawReport, RawRequest, IBCChannel, PriceResult

from pyband.proto.cosmos.base.tendermint.v1beta1.query_pb2 import GetLatestBlockResponse

from pyband.proto.tendermint.types.types_pb2 import (
    BlockID,
    PartSetHeader,
    Header,
    Data,
    Commit,
    CommitSig,
)

from pyband.proto.tendermint.version.types_pb2 import Consensus

from pyband.proto.tendermint.types.block_pb2 import Block

from pyband.proto.tendermint.types.evidence_pb2 import EvidenceList

from pyband.proto.cosmos.tx.v1beta1.service_pb2 import GetTxRequest, GetTxResponse

from pyband.proto.cosmos.tx.v1beta1.tx_pb2 import Tx, TxBody, AuthInfo, SignerInfo, ModeInfo, Fee

from pyband.proto.cosmos.base.abci.v1beta1.abci_pb2 import TxResponse, ABCIMessageLog, StringEvent, Attribute

from pyband.proto.cosmos.tx.signing.v1beta1.signing_pb2 import SIGN_MODE_DIRECT

# Google
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.any_pb2 import Any

from pyband.exceptions import NotFoundError, EmptyMsgError


class OracleServicer(OracleServicerBase):
    def DataSource(self, request: QueryDataSourceRequest, context) -> QueryDataSourceResponse:
        if request.data_source_id == 1:
            return QueryDataSourceResponse(
                data_source=DataSource(
                    owner="band1jfdmjkxs3hvddsf4ef2wmsmte3s5llqhxqgcfe",
                    name="DS1",
                    description="TBD",
                    filename="32ee6262d4a615f2c3ca0589c1c1af79212f24823453cb3f4cfff85b8d338045",
                    treasury="band1jfdmjkxs3hvddsf4ef2wmsmte3s5llqhxqgcfe",
                )
            )

    def OracleScript(self, request: QueryOracleScriptResponse, context) -> QueryOracleScriptResponse:
        if request.oracle_script_id == 1:
            return QueryOracleScriptResponse(
                oracle_script=OracleScript(
                    owner="band1m5lq9u533qaya4q3nfyl6ulzqkpkhge9q8tpzs",
                    name="Cryptocurrency Price in USD",
                    description="Oracle script that queries the average cryptocurrency price using current price data from CoinGecko, CryptoCompare, and Binance",
                    filename="a1f941e828bd8d5ea9c98e2cd3ff9ba8e52a8f63dca45bddbb2fdbfffebc7556",
                    schema="{symbol:string,multiplier:u64}/{px:u64}",
                    source_code_url="https://ipfs.io/ipfs/QmQqxHLszpbCy8Hk2ame3pPAxUUAyStBrVdGdDgrfAngAv",
                )
            )

    def Request(self, request: QueryRequestRequest, context) -> QueryRequestResponse:
        if request.request_id == 1:
            return QueryRequestResponse(
                request=Request(
                    oracle_script_id=1,
                    calldata=b"AAAAA0JUQwAAAAAAAAPo",
                    requested_validators=[
                        "bandvaloper1j9vk75jjty02elhwqqjehaspfslaem8pr20qst",
                    ],
                    min_count=1,
                    request_height=26525,
                    request_time=1620798812,
                    client_id="from_pyband",
                    raw_requests=[
                        RawRequest(external_id=1, data_source_id=1, calldata=b"QlRD"),
                        RawRequest(external_id=2, data_source_id=2, calldata=b"QlRD"),
                        RawRequest(external_id=3, data_source_id=3, calldata=b"QlRD"),
                    ],
                    ibc_channel=IBCChannel(
                        port_id="oracle",
                        channel_id="channel-2",
                    ),
                    execute_gas=300000,
                ),
                reports=[
                    {
                        "validator": "bandvaloper1j9vk75jjty02elhwqqjehaspfslaem8pr20qst",
                        "in_before_resolve": True,
                        "raw_reports": [
                            RawReport(external_id=1, exit_code=0, data=b"NTczMjcK"),
                            RawReport(external_id=2, exit_code=0, data=b"NTczMjcK"),
                            RawReport(external_id=3, exit_code=0, data=b"NTcyODYuMDE1Cg=="),
                        ],
                    },
                ],
                result=Result(
                    client_id="from_pyband",
                    oracle_script_id=1,
                    calldata=b"AAAAA0JUQwAAAAAAAAPo",
                    ask_count=2,
                    min_count=1,
                    request_id=6,
                    ans_count=2,
                    request_time=1620798812,
                    resolve_time=1620798814,
                    resolve_status="RESOLVE_STATUS_SUCCESS",
                    result=b"AAAAAANqiDo=",
                ),
            )

    def Reporters(self, request: QueryReportersRequest, context) -> QueryReportersResponse:
        return QueryReportersResponse(
            reporter=[
                "band1yyv5jkqaukq0ajqn7vhkyhpff7h6e99ja7gvwg",
                "band19nf0sqnjycnvpexlxs6hjz9qrhhlhsu9pdty0r",
                "band1fndxcmg0h5vhr8cph7gryryqfn9yqp90lysjtm",
                "band10ec0p96j60duce5qagju5axuja0rj8luqrzl0k",
                "band15pm9scujgkpwpy2xa2j53tvs9ylunjn0g73a9s",
                "band1cehe3sxk7f4rmvwdf6lxh3zexen7fn02zyltwy",
            ]
        )

    def RequestPrice(self, request: QueryRequestPriceRequest, context):
        # Assume that price = 10 will return price not found error
        if request.ask_count != 10:
            return QueryRequestPriceResponse(
                price_results=[
                    PriceResult(
                        symbol="ETH",
                        multiplier=1000000,
                        px=2317610000,
                        request_id=37653,
                        resolve_time=1625407289,
                    ),
                    PriceResult(
                        symbol="BTC",
                        multiplier=1000000,
                        px=35367670000,
                        request_id=37653,
                        resolve_time=1625407289,
                    ),
                    PriceResult(
                        symbol="USDT",
                        multiplier=1000000,
                        px=1000000,
                        request_id=37650,
                        resolve_time=1625407281,
                    ),
                ]
            )

    def RequestSearch(self, request: QueryRequestSearchRequest, context):
        return QueryRequestSearchResponse(
            request=QueryRequestResponse(
                request=Request(
                    oracle_script_id=47,
                    calldata=b"\000\000\000@BDE15735EDFA21E8C4484866C865177D13E88C5BD0B016CB3F5835613189B263\000\000\000\000#u\240S",
                    requested_validators=[
                        "bandvaloper1zl5925n5u24njn9axpygz8lhjl5a8v4cpkzx5g",
                        "bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                        "bandvaloper1e9sa38742tzhmandc4gkqve9zy8zc0yremaa3j",
                        "bandvaloper1qa4k43m4avza36kkal0vmsvccnpyyp6ltyp2l5",
                        "bandvaloper1t9vedyzsxewe6lhpf9vm47em2hly23xm6uqtec",
                        "bandvaloper1l2hchtyawk9tk43zzjrzr2lcd0zyxngcjdsshe",
                        "bandvaloper1d96u0qlvdp6vx3j6r33lujr93f7gdyy6erc839",
                        "bandvaloper1t659auvvukjtfn2h3hfp7usw0dqg6auhkwa9fs",
                    ],
                    min_count=11,
                    request_height=251543,
                    request_time=1625077316,
                    client_id="from_pyband_mumu_0",
                    raw_requests=[
                        RawRequest(
                            external_id=1,
                            data_source_id=83,
                            calldata=b"BDE15735EDFA21E8C4484866C865177D13E88C5BD0B016CB3F5835613189B263 594911315",
                        )
                    ],
                    execute_gas=3000000,
                ),
                reports=[
                    Report(
                        validator="bandvaloper1qa4k43m4avza36kkal0vmsvccnpyyp6ltyp2l5",
                        in_before_resolve=True,
                        raw_reports=[
                            RawReport(
                                external_id=1,
                                data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                            )
                        ],
                    ),
                    Report(
                        validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                        in_before_resolve=True,
                        raw_reports=[
                            RawReport(
                                external_id=1,
                                data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                            )
                        ],
                    ),
                    Report(
                        validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                        in_before_resolve=True,
                        raw_reports=[
                            RawReport(
                                external_id=1,
                                data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                            )
                        ],
                    ),
                    Report(
                        validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                        in_before_resolve=True,
                        raw_reports=[
                            RawReport(
                                external_id=1,
                                data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                            )
                        ],
                    ),
                    Report(
                        validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                        in_before_resolve=True,
                        raw_reports=[
                            RawReport(
                                external_id=1,
                                data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                            )
                        ],
                    ),
                ],
                result=Result(
                    client_id="from_pyband_mumu_0",
                    oracle_script_id=47,
                    calldata=b"\000\000\000@BDE15735EDFA21E8C4484866C865177D13E88C5BD0B016CB3F5835613189B263\000\000\000\000#u\240S",
                    ask_count=12,
                    min_count=11,
                    request_id=37635,
                    ans_count=12,
                    request_time=1625077316,
                    resolve_time=1625077324,
                    resolve_status=1,
                    result=b"\000\000\000@\313\022\372/\200fpH\305\367\204\020h9\220\2621\336\276#\024m\323\322\271\213Q\331-\244\364\326\310\002\202o.\305&\300\345\177\312T\t\216\023{\213\311\035\300\350z\0246\337\316\326\220 x\270\333",
                ),
            )
        )


class CosmosTransactionServicer(CosmosTxServicerBase):
    def GetTx(self, request: GetTxRequest, context) -> GetTxResponse:
        # Request id can come from request or report
        if request.hash == "txhash":
            return GetTxResponse(
                tx=Tx(
                    body=TxBody(
                        messages=[
                            Any(
                                type_url="/oracle.v1.MsgRequestData",
                                value=b"\010%\0220\000\000\000\005\000\000\000\003ETH\000\000\000\003BTC\000\000\000\004BAND\000\000\000\003MIR\000\000\000\003UNI\000\000\000\000\000\000\000d\030\020 \n*\014from_bandd_28\320\206\003@\340\247\022J+band1ky9tdhvr6669skylg02sv5ckvra84gn6vpfc8q",
                            )
                        ]
                    ),
                    auth_info=AuthInfo(
                        signer_infos=[
                            SignerInfo(
                                public_key=Any(
                                    type_url="/cosmos.crypto.secp256k1.PubKey",
                                    value=b"\n!\003\214\211\255\243\264\216\305\363,\370\332\214C\356\022yM?9\207B?\371\210\002\325\374\366\356C\021\223",
                                ),
                                mode_info=ModeInfo(single=ModeInfo.Single(mode=SIGN_MODE_DIRECT)),
                                sequence=478,
                            )
                        ],
                        fee=Fee(gas_limit=2000000),
                    ),
                    signatures=[
                        b'4\331\316\363\241L\342\217\201L"\311\002\036\324E\0163\377L\261\263Q\277\333\252\215\205\323,5L8D\254Q\376\312\314\261\243\020\214\213\325\316\314\226rw\177Y\026&E\r\344\312\n\321~\325\025\340'
                    ],
                ),
                tx_response=TxResponse(
                    height=686917,
                    txhash="AFC6BDDC7E7041B1AC21C26E25A52550689D148BE9A0D8E797E45DD753BF7FB3",
                    data="0A090A0772657175657374",
                    raw_log="[{'events':[{'type':'message','attributes':[{'key':'action','value':'request'}]},{'type':'raw_request','attributes':[{'key':'data_source_id','value':'61'},{'key':'data_source_hash','value':'07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef'},{'key':'external_id','value':'6'},{'key':'calldata','value':'ETH BTC'},{'key':'data_source_id','value':'57'},{'key':'data_source_hash','value':'61b369daa5c0918020a52165f6c7662d5b9c1eee915025cb3d2b9947a26e48c7'},{'key':'external_id','value':'0'},{'key':'calldata','value':'ETH BTC BAND'},{'key':'data_source_id','value':'62'},{'key':'data_source_hash','value':'107048da9dbf7960c79fb20e0585e080bb9be07d42a1ce09c5479bbada8d0289'},{'key':'external_id','value':'3'},{'key':'calldata','value':'ETH BTC BAND MIR UNI'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'5'},{'key':'calldata','value':'huobipro ETH BTC BAND'},{'key':'data_source_id','value':'59'},{'key':'data_source_hash','value':'5c011454981c473af3bf6ef93c76b36bfb6cc0ce5310a70a1ba569de3fc0c15d'},{'key':'external_id','value':'2'},{'key':'calldata','value':'ETH BTC BAND MIR UNI'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'4'},{'key':'calldata','value':'binance ETH BTC BAND MIR UNI'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'9'},{'key':'calldata','value':'bittrex ETH BTC'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'7'},{'key':'calldata','value':'kraken ETH BTC'},{'key':'data_source_id','value':'60'},{'key':'data_source_hash','value':'2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac'},{'key':'external_id','value':'8'},{'key':'calldata','value':'bitfinex ETH BTC'},{'key':'data_source_id','value':'58'},{'key':'data_source_hash','value':'7e6759fade717a06fb643392bfde837bfc3437da2ded54feed706e6cd35de461'},{'key':'external_id','value':'1'},{'key':'calldata','value':'ETH BTC BAND UNI'}]},{'type':'request','attributes':[{'key':'id','value':'154966'},{'key':'client_id','value':'from_bandd_2'},{'key':'oracle_script_id','value':'37'},{'key':'calldata','value':'0000000500000003455448000000034254430000000442414e44000000034d495200000003554e490000000000000064'},{'key':'ask_count','value':'16'},{'key':'min_count','value':'10'},{'key':'gas_used','value':'196024'},{'key':'validator','value':'bandvaloper18tjynh8v0kvf9lmjenx02fgltxk0c6jmm2wcjc'},{'key':'validator','value':'bandvaloper1h52l9shahsdzrduwtjt9exc349sehx4s2zydrv'},{'key':'validator','value':'bandvaloper1t0x8dv4frjnrnl0geegf9l5hrj9wa7qwmjrrwg'},{'key':'validator','value':'bandvaloper1kfj48adjsnrgu83lau6wc646q2uf65rf84tzus'},{'key':'validator','value':'bandvaloper1g4tfgzuxtnfzpnc7drk83n6r6ghkmzwsc7eglq'},{'key':'validator','value':'bandvaloper1w46umthap3cmvqarrznauy25mdhqu45tv8hq62'},{'key':'validator','value':'bandvaloper1a570h9e3rtvfhm030ta5hvel7e7e4lh4pgv8wj'},{'key':'validator','value':'bandvaloper12dzdxtd2mtnc37nfutwmj0lv8lsfgn6um0e5q5'},{'key':'validator','value':'bandvaloper19j74weeme5ehvmfnduz5swkxysz4twg92swxaf'},{'key':'validator','value':'bandvaloper1qudzmeu5yr7ryaq9spfpurptvlv4mxehe8x86e'},{'key':'validator','value':'bandvaloper1u6skdqfp3dcmvqfx28ej8v9nadf6mmpq6sp52a'},{'key':'validator','value':'bandvaloper106e65xpz88s5xvnlp5lqx98th9zvpptu7uj7zy'},{'key':'validator','value':'bandvaloper1u3c40nglllu4upuddlz6l59afq7uuz7lq6z977'},{'key':'validator','value':'bandvaloper1d0kcwzukkjl2w2nty3xerqpy3ypdrph67hxx4v'},{'key':'validator','value':'bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa'},{'key':'validator','value':'bandvaloper1dafxd4nacdry36tvsv6htaclkma4xhj6l9qrfv'}]}]}]",
                    logs=[
                        ABCIMessageLog(
                            events=[
                                StringEvent(type="message", attributes=[Attribute(key="action", value="request")]),
                                StringEvent(
                                    type="raw_request",
                                    attributes=[
                                        Attribute(key="data_source_id", value="61"),
                                        Attribute(
                                            key="data_source_hash",
                                            value="07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef",
                                        ),
                                        Attribute(key="external_id", value="6"),
                                    ],
                                ),
                                StringEvent(
                                    type="report",
                                    attributes=[
                                        Attribute(key="id", value="154966"),
                                        Attribute(key="client_id", value="from_bandd_2"),
                                        Attribute(key="oracle_script_id", value="37"),
                                    ],
                                ),
                            ]
                        )
                    ],
                    gas_wanted=2000000,
                    gas_used=1059525,
                    tx=Any(
                        type_url="/cosmos.tx.v1beta1.Tx",
                        value=b'\n\233\001\n\230\001\n\031/oracle.v1.MsgRequestData\022{\010%\0220\000\000\000\005\000\000\000\003ETH\000\000\000\003BTC\000\000\000\004BAND\000\000\000\003MIR\000\000\000\003UNI\000\000\000\000\000\000\000d\030\020 \n*\014from_bandd_28\320\206\003@\340\247\022J+band1ky9tdhvr6669skylg02sv5ckvra84gn6vpfc8q\022Y\nQ\nF\n\037/cosmos.crypto.secp256k1.PubKey\022#\n!\003\214\211\255\243\264\216\305\363,\370\332\214C\356\022yM?9\207B?\371\210\002\325\374\366\356C\021\223\022\004\n\002\010\001\030\336\003\022\004\020\200\211z\032@4\331\316\363\241L\342\217\201L"\311\002\036\324E\0163\377L\261\263Q\277\333\252\215\205\323,5L8D\254Q\376\312\314\261\243\020\214\213\325\316\314\226rw\177Y\026&E\r\344\312\n\321~\325\025\340',
                    ),
                    timestamp="2021-06-04T06:07:37Z",
                ),
            )
        elif request.hash == "txhashRequestMultiId":
            return GetTxResponse(
                tx=Tx(
                    body=TxBody(
                        messages=[
                            Any(
                                type_url="/oracle.v1.MsgRequestData",
                                value=b"\010%\0220\000\000\000\005\000\000\000\003ETH\000\000\000\003BTC\000\000\000\004BAND\000\000\000\003MIR\000\000\000\003UNI\000\000\000\000\000\000\000d\030\020 \n*\014from_bandd_28\320\206\003@\340\247\022J+band1ky9tdhvr6669skylg02sv5ckvra84gn6vpfc8q",
                            )
                        ]
                    ),
                    auth_info=AuthInfo(
                        signer_infos=[
                            SignerInfo(
                                public_key=Any(
                                    type_url="/cosmos.crypto.secp256k1.PubKey",
                                    value=b"\n!\003\214\211\255\243\264\216\305\363,\370\332\214C\356\022yM?9\207B?\371\210\002\325\374\366\356C\021\223",
                                ),
                                mode_info=ModeInfo(single=ModeInfo.Single(mode=SIGN_MODE_DIRECT)),
                                sequence=478,
                            )
                        ],
                        fee=Fee(gas_limit=2000000),
                    ),
                    signatures=[
                        b'4\331\316\363\241L\342\217\201L"\311\002\036\324E\0163\377L\261\263Q\277\333\252\215\205\323,5L8D\254Q\376\312\314\261\243\020\214\213\325\316\314\226rw\177Y\026&E\r\344\312\n\321~\325\025\340'
                    ],
                ),
                tx_response=TxResponse(
                    height=686917,
                    txhash="AFC6BDDC7E7041B1AC21C26E25A52550689D148BE9A0D8E797E45DD753BF7FB3",
                    data="0A090A0772657175657374",
                    raw_log='[{"events":[{"type":"message","attributes":[{"key":"action","value":"request"}]},{"type":"raw_request","attributes":[{"key":"data_source_id","value":"61"},{"key":"data_source_hash","value":"07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef"},{"key":"external_id","value":"6"},{"key":"calldata","value":"ETH BTC"},{"key":"data_source_id","value":"57"},{"key":"data_source_hash","value":"61b369daa5c0918020a52165f6c7662d5b9c1eee915025cb3d2b9947a26e48c7"},{"key":"external_id","value":"0"},{"key":"calldata","value":"ETH BTC BAND"},{"key":"data_source_id","value":"62"},{"key":"data_source_hash","value":"107048da9dbf7960c79fb20e0585e080bb9be07d42a1ce09c5479bbada8d0289"},{"key":"external_id","value":"3"},{"key":"calldata","value":"ETH BTC BAND MIR UNI"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"5"},{"key":"calldata","value":"huobipro ETH BTC BAND"},{"key":"data_source_id","value":"59"},{"key":"data_source_hash","value":"5c011454981c473af3bf6ef93c76b36bfb6cc0ce5310a70a1ba569de3fc0c15d"},{"key":"external_id","value":"2"},{"key":"calldata","value":"ETH BTC BAND MIR UNI"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"4"},{"key":"calldata","value":"binance ETH BTC BAND MIR UNI"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"9"},{"key":"calldata","value":"bittrex ETH BTC"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"7"},{"key":"calldata","value":"kraken ETH BTC"},{"key":"data_source_id","value":"60"},{"key":"data_source_hash","value":"2e588de76a58338125022bc42b460072300aebbcc4acaf55f91755c1c1799bac"},{"key":"external_id","value":"8"},{"key":"calldata","value":"bitfinex ETH BTC"},{"key":"data_source_id","value":"58"},{"key":"data_source_hash","value":"7e6759fade717a06fb643392bfde837bfc3437da2ded54feed706e6cd35de461"},{"key":"external_id","value":"1"},{"key":"calldata","value":"ETH BTC BAND UNI"}]},{"type":"request","attributes":[{"key":"id","value":"154966"},{"key":"client_id","value":"from_bandd_2"},{"key":"oracle_script_id","value":"37"},{"key":"calldata","value":"0000000500000003455448000000034254430000000442414e44000000034d495200000003554e490000000000000064"},{"key":"ask_count","value":"16"},{"key":"min_count","value":"10"},{"key":"gas_used","value":"196024"},{"key":"validator","value":"bandvaloper18tjynh8v0kvf9lmjenx02fgltxk0c6jmm2wcjc"},{"key":"validator","value":"bandvaloper1h52l9shahsdzrduwtjt9exc349sehx4s2zydrv"},{"key":"validator","value":"bandvaloper1t0x8dv4frjnrnl0geegf9l5hrj9wa7qwmjrrwg"},{"key":"validator","value":"bandvaloper1kfj48adjsnrgu83lau6wc646q2uf65rf84tzus"},{"key":"validator","value":"bandvaloper1g4tfgzuxtnfzpnc7drk83n6r6ghkmzwsc7eglq"},{"key":"validator","value":"bandvaloper1w46umthap3cmvqarrznauy25mdhqu45tv8hq62"},{"key":"validator","value":"bandvaloper1a570h9e3rtvfhm030ta5hvel7e7e4lh4pgv8wj"},{"key":"validator","value":"bandvaloper12dzdxtd2mtnc37nfutwmj0lv8lsfgn6um0e5q5"},{"key":"validator","value":"bandvaloper19j74weeme5ehvmfnduz5swkxysz4twg92swxaf"},{"key":"validator","value":"bandvaloper1qudzmeu5yr7ryaq9spfpurptvlv4mxehe8x86e"},{"key":"validator","value":"bandvaloper1u6skdqfp3dcmvqfx28ej8v9nadf6mmpq6sp52a"},{"key":"validator","value":"bandvaloper106e65xpz88s5xvnlp5lqx98th9zvpptu7uj7zy"},{"key":"validator","value":"bandvaloper1u3c40nglllu4upuddlz6l59afq7uuz7lq6z977"},{"key":"validator","value":"bandvaloper1d0kcwzukkjl2w2nty3xerqpy3ypdrph67hxx4v"},{"key":"validator","value":"bandvaloper1nlepx7xg53fsy6vslrss6adtmtl8a33kusv7fa"},{"key":"validator","value":"bandvaloper1dafxd4nacdry36tvsv6htaclkma4xhj6l9qrfv"}]}]}]',
                    logs=[
                        ABCIMessageLog(
                            events=[
                                StringEvent(type="message", attributes=[Attribute(key="action", value="request")]),
                                StringEvent(
                                    type="raw_request",
                                    attributes=[
                                        Attribute(key="data_source_id", value="61"),
                                        Attribute(
                                            key="data_source_hash",
                                            value="07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef",
                                        ),
                                        Attribute(key="external_id", value="6"),
                                    ],
                                ),
                                StringEvent(
                                    type="request",
                                    attributes=[
                                        Attribute(key="id", value="111111"),
                                        Attribute(key="client_id", value="from_bandd_2"),
                                        Attribute(key="oracle_script_id", value="37"),
                                    ],
                                ),
                            ]
                        ),
                        ABCIMessageLog(
                            events=[
                                StringEvent(type="message", attributes=[Attribute(key="action", value="request")]),
                                StringEvent(
                                    type="raw_request",
                                    attributes=[
                                        Attribute(key="data_source_id", value="61"),
                                        Attribute(
                                            key="data_source_hash",
                                            value="07be7bd61667327aae10b7a13a542c7dfba31b8f4c52b0b60bf9c7b11b1a72ef",
                                        ),
                                        Attribute(key="external_id", value="6"),
                                    ],
                                ),
                                StringEvent(
                                    type="request",
                                    attributes=[
                                        Attribute(key="id", value="222222"),
                                        Attribute(key="client_id", value="from_bandd_2"),
                                        Attribute(key="oracle_script_id", value="37"),
                                    ],
                                ),
                            ]
                        ),
                    ],
                    gas_wanted=2000000,
                    gas_used=1059525,
                    tx=Any(
                        type_url="/cosmos.tx.v1beta1.Tx",
                        value=b'\n\233\001\n\230\001\n\031/oracle.v1.MsgRequestData\022{\010%\0220\000\000\000\005\000\000\000\003ETH\000\000\000\003BTC\000\000\000\004BAND\000\000\000\003MIR\000\000\000\003UNI\000\000\000\000\000\000\000d\030\020 \n*\014from_bandd_28\320\206\003@\340\247\022J+band1ky9tdhvr6669skylg02sv5ckvra84gn6vpfc8q\022Y\nQ\nF\n\037/cosmos.crypto.secp256k1.PubKey\022#\n!\003\214\211\255\243\264\216\305\363,\370\332\214C\356\022yM?9\207B?\371\210\002\325\374\366\356C\021\223\022\004\n\002\010\001\030\336\003\022\004\020\200\211z\032@4\331\316\363\241L\342\217\201L"\311\002\036\324E\0163\377L\261\263Q\277\333\252\215\205\323,5L8D\254Q\376\312\314\261\243\020\214\213\325\316\314\226rw\177Y\026&E\r\344\312\n\321~\325\025\340',
                    ),
                    timestamp="2021-06-04T06:07:37Z",
                ),
            )


class AuthServicer(AuthServicerBase):
    def Account(self, request, context) -> QueryAccountResponse:
        if request.address == "noAccount":
            raise NotFoundError("Account not found")
        # Account exist
        acc = BaseAccount(account_number=1)
        any = Any()
        any.Pack(acc)
        return QueryAccountResponse(account=any)


class TendermintServicer(TendermintServicerBase):
    def GetLatestBlock(self, request, context) -> GetLatestBlockResponse:
        return GetLatestBlockResponse(
            block_id=BlockID(
                hash=b"391E99908373F8590C928E0619956DA3D87EB654445DA4F25A185C9718561D53",
                part_set_header=PartSetHeader(
                    total=1,
                    hash=b"9DC1DB39B7DDB97DE353DFB2898198BAADEFB7DF8090BF22678714F769D69F42",
                ),
            ),
            block=Block(
                header=Header(
                    version=Consensus(block=10, app=0),
                    chain_id="bandchain",
                    height=1032007,
                    time=Timestamp().FromJsonString("2020-11-05T09:15:18.445494105Z"),
                    last_block_id=BlockID(
                        hash=b"4BC01E257662B5F9337D615D06D5D19D8D79F7BA5A4022A85B4DC4ED3C59F7CA",
                        part_set_header=PartSetHeader(
                            total=1,
                            hash=b"6471C0A51FB7043171EAA76CAFA900B36A4494F47F975980732529D247E8EBA5",
                        ),
                    ),
                    last_commit_hash=b"17B2CE4ABA910E85847537F1323DB95C9F16C20C60E9B9BBB04C633C3125BD92",
                    data_hash=b"EFE5E3F549554FEE8EB9B393740C250D74580427A96A175ABB105806039CFFE2",
                    validators_hash=b"E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151",
                    next_validators_hash=b"E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151",
                    consensus_hash=b"0EAA6F4F4B8BD1CC222D93BBD391D07F074DE6BE5A52C6964875BB355B7D0B45",
                    app_hash=b"6E2B1ECE9D912D86C25182E8B7419583ABCE978BFC66DC2556BB0D06A8D528EF",
                    last_results_hash=b"",
                    evidence_hash=b"",
                    proposer_address=b"BDB6A0728C8DFE2124536F16F2BA428FE767A8F9",
                ),
                data=Data(
                    txs=[
                        b"yAEoKBapCj5CcI40CAESDwAAAANCVEMAAAAAAAAAARgEIAMqC2Zyb21fcHliYW5kMhSQ78AMmxLrubEOPhhIwKK5oyk9oBIQCgoKBXViYW5kEgEwEMCEPRpqCibrWumHIQP+cIvaZlJP0sa86QaC44VVqFHgPSruT2KbBd6Q9R7ZvBJANbPqLRAgwwULWWwb5O2/eb6ddtDr65kRFgDcOTTGIqQS5Iz1NvHWHfkPKRoM8egErMsgE9YnuE+pAqoc/YvNfiIEVEVTVA=="
                    ]
                ),
                evidence=EvidenceList(evidence=None),
                last_commit=Commit(
                    height=1032006,
                    round=0,
                    block_id=BlockID(
                        hash=b"4BC01E257662B5F9337D615D06D5D19D8D79F7BA5A4022A85B4DC4ED3C59F7CA",
                        part_set_header=PartSetHeader(
                            total=1,
                            hash=b"6471C0A51FB7043171EAA76CAFA900B36A4494F47F975980732529D247E8EBA5",
                        ),
                    ),
                    signatures=[
                        CommitSig(
                            block_id_flag=3,
                            validator_address=b"5179B0BB203248E03D2A1342896133B5C58E1E44",
                            timestamp=Timestamp().FromJsonString("2020-11-05T09:15:18.53815896Z"),
                            signature=b"TZY24CKwZOE8wqfE0NM3qzkQ7qCpCrGEHNZdf8n31L4otZzbKGfOL05kGtBsGkTnZkVv7aJmrJ7XbvIzv0SREQ==",
                        ),
                        CommitSig(
                            block_id_flag=3,
                            validator_address=b"5179B0BB203248E03D2A1342896133B5C58E1E44",
                            timestamp=Timestamp().FromJsonString("2020-11-05T09:15:18.53815896Z"),
                            signature=b"TZY24CKwZOE8wqfE0NM3qzkQ7qCpCrGEHNZdf8n31L4otZzbKGfOL05kGtBsGkTnZkVv7aJmrJ7XbvIzv0SREQ==",
                        ),
                    ],
                ),
            ),
        )


@pytest.fixture(scope="module")
def pyband_client(_grpc_server, grpc_addr):
    from pyband.proto.oracle.v1.query_pb2_grpc import add_QueryServicer_to_server as add_oracle
    from pyband.proto.cosmos.tx.v1beta1.service_pb2_grpc import add_ServiceServicer_to_server as add_cosmos_tx
    from pyband.proto.cosmos.auth.v1beta1.query_pb2_grpc import add_QueryServicer_to_server as add_auth
    from pyband.proto.cosmos.base.tendermint.v1beta1.query_pb2_grpc import (
        add_ServiceServicer_to_server as add_tendermint,
    )

    add_oracle(OracleServicer(), _grpc_server)
    add_cosmos_tx(CosmosTransactionServicer(), _grpc_server)
    add_auth(AuthServicer(), _grpc_server)
    add_tendermint(TendermintServicer(), _grpc_server)

    _grpc_server.add_insecure_port(grpc_addr)
    _grpc_server.start()

    from pyband.client import Client

    yield Client(grpc_addr)
    _grpc_server.stop(grace=None)


def test_get_data_source_success(pyband_client):
    data_source = pyband_client.get_data_source(1)
    mock_result = DataSource(
        owner="band1jfdmjkxs3hvddsf4ef2wmsmte3s5llqhxqgcfe",
        name="DS1",
        description="TBD",
        filename="32ee6262d4a615f2c3ca0589c1c1af79212f24823453cb3f4cfff85b8d338045",
        treasury="band1jfdmjkxs3hvddsf4ef2wmsmte3s5llqhxqgcfe",
    )
    assert data_source == mock_result


def test_get_data_source_invalid(pyband_client):
    with pytest.raises(grpc.RpcError):
        pyband_client.get_data_source(0)


def test_get_data_source_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        pyband_client.get_data_source("hi")

    with pytest.raises(ValueError):
        pyband_client.get_data_source(-1)


def test_get_oracle_script_success(pyband_client):
    oracle_script = pyband_client.get_oracle_script(1)
    mock_result = OracleScript(
        owner="band1m5lq9u533qaya4q3nfyl6ulzqkpkhge9q8tpzs",
        name="Cryptocurrency Price in USD",
        description="Oracle script that queries the average cryptocurrency price using current price data from CoinGecko, CryptoCompare, and Binance",
        filename="a1f941e828bd8d5ea9c98e2cd3ff9ba8e52a8f63dca45bddbb2fdbfffebc7556",
        schema="{symbol:string,multiplier:u64}/{px:u64}",
        source_code_url="https://ipfs.io/ipfs/QmQqxHLszpbCy8Hk2ame3pPAxUUAyStBrVdGdDgrfAngAv",
    )
    assert oracle_script == mock_result


def test_get_oracle_script_invalid(pyband_client):
    with pytest.raises(grpc.RpcError):
        pyband_client.get_oracle_script(0)


def test_get_oracle_script_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        pyband_client.get_oracle_script("hi")

    with pytest.raises(ValueError):
        pyband_client.get_oracle_script(-1)


def test_get_request_by_id_success(pyband_client):
    response = pyband_client.get_request_by_id(1)
    mock_result = QueryRequestResponse(
        request=Request(
            oracle_script_id=1,
            calldata=b"AAAAA0JUQwAAAAAAAAPo",
            requested_validators=[
                "bandvaloper1j9vk75jjty02elhwqqjehaspfslaem8pr20qst",
            ],
            min_count=1,
            request_height=26525,
            request_time=1620798812,
            client_id="from_pyband",
            raw_requests=[
                RawRequest(external_id=1, data_source_id=1, calldata=b"QlRD"),
                RawRequest(external_id=2, data_source_id=2, calldata=b"QlRD"),
                RawRequest(external_id=3, data_source_id=3, calldata=b"QlRD"),
            ],
            ibc_channel=IBCChannel(
                port_id="oracle",
                channel_id="channel-2",
            ),
            execute_gas=300000,
        ),
        reports=[
            {
                "validator": "bandvaloper1j9vk75jjty02elhwqqjehaspfslaem8pr20qst",
                "in_before_resolve": True,
                "raw_reports": [
                    RawReport(external_id=1, exit_code=0, data=b"NTczMjcK"),
                    RawReport(external_id=2, exit_code=0, data=b"NTczMjcK"),
                    RawReport(external_id=3, exit_code=0, data=b"NTcyODYuMDE1Cg=="),
                ],
            },
        ],
        result=Result(
            client_id="from_pyband",
            oracle_script_id=1,
            calldata=b"AAAAA0JUQwAAAAAAAAPo",
            ask_count=2,
            min_count=1,
            request_id=6,
            ans_count=2,
            request_time=1620798812,
            resolve_time=1620798814,
            resolve_status="RESOLVE_STATUS_SUCCESS",
            result=b"AAAAAANqiDo=",
        ),
    )
    assert response == mock_result


def test_get_request_by_id_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        pyband_client.get_request_by_id("hi")

    with pytest.raises(ValueError):
        pyband_client.get_request_by_id(-1)


def test_get_request_by_id_not_found(pyband_client):
    with pytest.raises(grpc.RpcError):
        pyband_client.get_request_by_id(1234556)


def test_get_request_by_id_invalid(pyband_client):
    with pytest.raises(grpc.RpcError):
        pyband_client.get_request_by_id(0)


def test_get_reporters_success(pyband_client):
    reporters = pyband_client.get_reporters("validator")
    mock_result = [
        "band1yyv5jkqaukq0ajqn7vhkyhpff7h6e99ja7gvwg",
        "band19nf0sqnjycnvpexlxs6hjz9qrhhlhsu9pdty0r",
        "band1fndxcmg0h5vhr8cph7gryryqfn9yqp90lysjtm",
        "band10ec0p96j60duce5qagju5axuja0rj8luqrzl0k",
        "band15pm9scujgkpwpy2xa2j53tvs9ylunjn0g73a9s",
        "band1cehe3sxk7f4rmvwdf6lxh3zexen7fn02zyltwy",
    ]
    assert reporters == mock_result


def test_get_reporters_invalid_input(pyband_client):
    with pytest.raises(TypeError):
        pyband_client.get_reporters(1)


def test_get_latest_block(pyband_client):
    latest_block = pyband_client.get_latest_block()
    mock_result = GetLatestBlockResponse(
        block_id=BlockID(
            hash=b"391E99908373F8590C928E0619956DA3D87EB654445DA4F25A185C9718561D53",
            part_set_header=PartSetHeader(
                total=1,
                hash=b"9DC1DB39B7DDB97DE353DFB2898198BAADEFB7DF8090BF22678714F769D69F42",
            ),
        ),
        block=Block(
            header=Header(
                version=Consensus(block=10, app=0),
                chain_id="bandchain",
                height=1032007,
                time=Timestamp().FromJsonString("2020-11-05T09:15:18.445494105Z"),
                last_block_id=BlockID(
                    hash=b"4BC01E257662B5F9337D615D06D5D19D8D79F7BA5A4022A85B4DC4ED3C59F7CA",
                    part_set_header=PartSetHeader(
                        total=1,
                        hash=b"6471C0A51FB7043171EAA76CAFA900B36A4494F47F975980732529D247E8EBA5",
                    ),
                ),
                last_commit_hash=b"17B2CE4ABA910E85847537F1323DB95C9F16C20C60E9B9BBB04C633C3125BD92",
                data_hash=b"EFE5E3F549554FEE8EB9B393740C250D74580427A96A175ABB105806039CFFE2",
                validators_hash=b"E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151",
                next_validators_hash=b"E3F0EA129867E1AB4D7D6A97C23771D4D89B9E4DFE0A5B11E03B681244E00151",
                consensus_hash=b"0EAA6F4F4B8BD1CC222D93BBD391D07F074DE6BE5A52C6964875BB355B7D0B45",
                app_hash=b"6E2B1ECE9D912D86C25182E8B7419583ABCE978BFC66DC2556BB0D06A8D528EF",
                last_results_hash=b"",
                evidence_hash=b"",
                proposer_address=b"BDB6A0728C8DFE2124536F16F2BA428FE767A8F9",
            ),
            data=Data(
                txs=[
                    b"yAEoKBapCj5CcI40CAESDwAAAANCVEMAAAAAAAAAARgEIAMqC2Zyb21fcHliYW5kMhSQ78AMmxLrubEOPhhIwKK5oyk9oBIQCgoKBXViYW5kEgEwEMCEPRpqCibrWumHIQP+cIvaZlJP0sa86QaC44VVqFHgPSruT2KbBd6Q9R7ZvBJANbPqLRAgwwULWWwb5O2/eb6ddtDr65kRFgDcOTTGIqQS5Iz1NvHWHfkPKRoM8egErMsgE9YnuE+pAqoc/YvNfiIEVEVTVA=="
                ]
            ),
            evidence=EvidenceList(evidence=None),
            last_commit=Commit(
                height=1032006,
                round=0,
                block_id=BlockID(
                    hash=b"4BC01E257662B5F9337D615D06D5D19D8D79F7BA5A4022A85B4DC4ED3C59F7CA",
                    part_set_header=PartSetHeader(
                        total=1,
                        hash=b"6471C0A51FB7043171EAA76CAFA900B36A4494F47F975980732529D247E8EBA5",
                    ),
                ),
                signatures=[
                    CommitSig(
                        block_id_flag=3,
                        validator_address=b"5179B0BB203248E03D2A1342896133B5C58E1E44",
                        timestamp=Timestamp().FromJsonString("2020-11-05T09:15:18.53815896Z"),
                        signature=b"TZY24CKwZOE8wqfE0NM3qzkQ7qCpCrGEHNZdf8n31L4otZzbKGfOL05kGtBsGkTnZkVv7aJmrJ7XbvIzv0SREQ==",
                    ),
                    CommitSig(
                        block_id_flag=3,
                        validator_address=b"5179B0BB203248E03D2A1342896133B5C58E1E44",
                        timestamp=Timestamp().FromJsonString("2020-11-05T09:15:18.53815896Z"),
                        signature=b"TZY24CKwZOE8wqfE0NM3qzkQ7qCpCrGEHNZdf8n31L4otZzbKGfOL05kGtBsGkTnZkVv7aJmrJ7XbvIzv0SREQ==",
                    ),
                ],
            ),
        ),
    )
    assert latest_block == mock_result


def test_get_account_success(pyband_client):
    account = pyband_client.get_account("xxx")
    assert account.account_number == 1


def test_get_account_not_exist(pyband_client):
    account = pyband_client.get_account("noAccount")
    assert account == None


def test_get_account_invalid_input(pyband_client):
    account = pyband_client.get_account(2)
    assert account == None


def test_get_req_id_by_tx_hash_success(pyband_client):
    reqId = pyband_client.get_request_id_by_tx_hash("txhash")
    assert reqId == [154966]


def test_get_req_id_by_tx_hash_invalid_input(pyband_client):
    reqId = pyband_client.get_request_id_by_tx_hash(b"txhashRequestMultiId")
    assert reqId == [111111, 222222]


def test_get_chain_id(pyband_client):
    chain_id = pyband_client.get_chain_id()
    assert chain_id == "bandchain"


def test_get_reference_data_success(pyband_client):
    [reference_data1, reference_data2] = pyband_client.get_reference_data(["ETH/USD", "BTC/USDT"], 3, 4)
    assert reference_data1.pair == "ETH/USD"
    assert reference_data2.pair == "BTC/USDT"
    assert reference_data1.rate == 2317.61
    assert reference_data2.rate == 35367.67
    assert type(reference_data1.updated_at.base) == int
    assert type(reference_data1.updated_at.quote) == int
    assert type(reference_data2.updated_at.base) == int
    assert type(reference_data2.updated_at.quote) == int


# Assume that this input price will return price not found error
def test_get_reference_data_wrong_price(pyband_client):
    with pytest.raises(grpc.RpcError):
        pyband_client.get_reference_data(["ETH/USDT", "BTC/USDT"], 3, 10)


def test_get_reference_data_empty_paires(pyband_client):
    with pytest.raises(EmptyMsgError, match="Pairs are required"):
        pyband_client.get_reference_data([], 3, 4)


def test_get_latest_request_success(pyband_client):
    latest_request = pyband_client.get_latest_request(
        47,
        "0000004042444531353733354544464132314538433434383438363643383635313737443133453838433542443042303136434233463538333536313331383942323633000000002375a053",
        11,
        12,
    )
    mock_result = QueryRequestSearchResponse(
        request=QueryRequestResponse(
            request=Request(
                oracle_script_id=47,
                calldata=b"\000\000\000@BDE15735EDFA21E8C4484866C865177D13E88C5BD0B016CB3F5835613189B263\000\000\000\000#u\240S",
                requested_validators=[
                    "bandvaloper1zl5925n5u24njn9axpygz8lhjl5a8v4cpkzx5g",
                    "bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                    "bandvaloper1e9sa38742tzhmandc4gkqve9zy8zc0yremaa3j",
                    "bandvaloper1qa4k43m4avza36kkal0vmsvccnpyyp6ltyp2l5",
                    "bandvaloper1t9vedyzsxewe6lhpf9vm47em2hly23xm6uqtec",
                    "bandvaloper1l2hchtyawk9tk43zzjrzr2lcd0zyxngcjdsshe",
                    "bandvaloper1d96u0qlvdp6vx3j6r33lujr93f7gdyy6erc839",
                    "bandvaloper1t659auvvukjtfn2h3hfp7usw0dqg6auhkwa9fs",
                ],
                min_count=11,
                request_height=251543,
                request_time=1625077316,
                client_id="from_pyband_mumu_0",
                raw_requests=[
                    RawRequest(
                        external_id=1,
                        data_source_id=83,
                        calldata=b"BDE15735EDFA21E8C4484866C865177D13E88C5BD0B016CB3F5835613189B263 594911315",
                    )
                ],
                execute_gas=3000000,
            ),
            reports=[
                Report(
                    validator="bandvaloper1qa4k43m4avza36kkal0vmsvccnpyyp6ltyp2l5",
                    in_before_resolve=True,
                    raw_reports=[
                        RawReport(
                            external_id=1,
                            data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                        )
                    ],
                ),
                Report(
                    validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                    in_before_resolve=True,
                    raw_reports=[
                        RawReport(
                            external_id=1,
                            data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                        )
                    ],
                ),
                Report(
                    validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                    in_before_resolve=True,
                    raw_reports=[
                        RawReport(
                            external_id=1,
                            data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                        )
                    ],
                ),
                Report(
                    validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                    in_before_resolve=True,
                    raw_reports=[
                        RawReport(
                            external_id=1,
                            data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                        )
                    ],
                ),
                Report(
                    validator="bandvaloper1p46uhvdk8vr829v747v85hst3mur2dzlhfemmz",
                    in_before_resolve=True,
                    raw_reports=[
                        RawReport(
                            external_id=1,
                            data=b"cb12fa2f80667048c5f78410683990b231debe23146dd3d2b98b51d92da4f4d6c802826f2ec526c0e57fca54098e137b8bc91dc0e87a1436dfced6902078b8db\n",
                        )
                    ],
                ),
            ],
            result=Result(
                client_id="from_pyband_mumu_0",
                oracle_script_id=47,
                calldata=b"\000\000\000@BDE15735EDFA21E8C4484866C865177D13E88C5BD0B016CB3F5835613189B263\000\000\000\000#u\240S",
                ask_count=12,
                min_count=11,
                request_id=37635,
                ans_count=12,
                request_time=1625077316,
                resolve_time=1625077324,
                resolve_status=1,
                result=b"\000\000\000@\313\022\372/\200fpH\305\367\204\020h9\220\2621\336\276#\024m\323\322\271\213Q\331-\244\364\326\310\002\202o.\305&\300\345\177\312T\t\216\023{\213\311\035\300\350z\0246\337\316\326\220 x\270\333",
            ),
        )
    )
    assert latest_request == mock_result
