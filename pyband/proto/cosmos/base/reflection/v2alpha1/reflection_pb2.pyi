"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

# AppDescriptor describes a cosmos-sdk based application
class AppDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AUTHN_FIELD_NUMBER: builtins.int
    CHAIN_FIELD_NUMBER: builtins.int
    CODEC_FIELD_NUMBER: builtins.int
    CONFIGURATION_FIELD_NUMBER: builtins.int
    QUERY_SERVICES_FIELD_NUMBER: builtins.int
    TX_FIELD_NUMBER: builtins.int
    # AuthnDescriptor provides information on how to authenticate transactions on the application
    # NOTE: experimental and subject to change in future releases.
    @property
    def authn(self) -> global___AuthnDescriptor: ...
    # chain provides the chain descriptor
    @property
    def chain(self) -> global___ChainDescriptor: ...
    # codec provides metadata information regarding codec related types
    @property
    def codec(self) -> global___CodecDescriptor: ...
    # configuration provides metadata information regarding the sdk.Config type
    @property
    def configuration(self) -> global___ConfigurationDescriptor: ...
    # query_services provides metadata information regarding the available queriable endpoints
    @property
    def query_services(self) -> global___QueryServicesDescriptor: ...
    # tx provides metadata information regarding how to send transactions to the given application
    @property
    def tx(self) -> global___TxDescriptor: ...
    def __init__(self,
        *,
        authn : typing.Optional[global___AuthnDescriptor] = ...,
        chain : typing.Optional[global___ChainDescriptor] = ...,
        codec : typing.Optional[global___CodecDescriptor] = ...,
        configuration : typing.Optional[global___ConfigurationDescriptor] = ...,
        query_services : typing.Optional[global___QueryServicesDescriptor] = ...,
        tx : typing.Optional[global___TxDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"authn",b"authn",u"chain",b"chain",u"codec",b"codec",u"configuration",b"configuration",u"query_services",b"query_services",u"tx",b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"authn",b"authn",u"chain",b"chain",u"codec",b"codec",u"configuration",b"configuration",u"query_services",b"query_services",u"tx",b"tx"]) -> None: ...
global___AppDescriptor = AppDescriptor

# TxDescriptor describes the accepted transaction type
class TxDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FULLNAME_FIELD_NUMBER: builtins.int
    MSGS_FIELD_NUMBER: builtins.int
    # fullname is the protobuf fullname of the raw transaction type (for instance the tx.Tx type)
    # it is not meant to support polymorphism of transaction types, it is supposed to be used by
    # reflection clients to understand if they can handle a specific transaction type in an application.
    fullname: typing.Text = ...
    # msgs lists the accepted application messages (sdk.Msg)
    @property
    def msgs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MsgDescriptor]: ...
    def __init__(self,
        *,
        fullname : typing.Text = ...,
        msgs : typing.Optional[typing.Iterable[global___MsgDescriptor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fullname",b"fullname",u"msgs",b"msgs"]) -> None: ...
global___TxDescriptor = TxDescriptor

# AuthnDescriptor provides information on how to sign transactions without relying
# on the online RPCs GetTxMetadata and CombineUnsignedTxAndSignatures
class AuthnDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SIGN_MODES_FIELD_NUMBER: builtins.int
    # sign_modes defines the supported signature algorithm
    @property
    def sign_modes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SigningModeDescriptor]: ...
    def __init__(self,
        *,
        sign_modes : typing.Optional[typing.Iterable[global___SigningModeDescriptor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"sign_modes",b"sign_modes"]) -> None: ...
global___AuthnDescriptor = AuthnDescriptor

# SigningModeDescriptor provides information on a signing flow of the application
# NOTE(fdymylja): here we could go as far as providing an entire flow on how
# to sign a message given a SigningModeDescriptor, but it's better to think about
# this another time
class SigningModeDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    NUMBER_FIELD_NUMBER: builtins.int
    AUTHN_INFO_PROVIDER_METHOD_FULLNAME_FIELD_NUMBER: builtins.int
    # name defines the unique name of the signing mode
    name: typing.Text = ...
    # number is the unique int32 identifier for the sign_mode enum
    number: builtins.int = ...
    # authn_info_provider_method_fullname defines the fullname of the method to call to get
    # the metadata required to authenticate using the provided sign_modes
    authn_info_provider_method_fullname: typing.Text = ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        number : builtins.int = ...,
        authn_info_provider_method_fullname : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"authn_info_provider_method_fullname",b"authn_info_provider_method_fullname",u"name",b"name",u"number",b"number"]) -> None: ...
global___SigningModeDescriptor = SigningModeDescriptor

# ChainDescriptor describes chain information of the application
class ChainDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ID_FIELD_NUMBER: builtins.int
    # id is the chain id
    id: typing.Text = ...
    def __init__(self,
        *,
        id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"id",b"id"]) -> None: ...
global___ChainDescriptor = ChainDescriptor

# CodecDescriptor describes the registered interfaces and provides metadata information on the types
class CodecDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    INTERFACES_FIELD_NUMBER: builtins.int
    # interfaces is a list of the registerted interfaces descriptors
    @property
    def interfaces(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InterfaceDescriptor]: ...
    def __init__(self,
        *,
        interfaces : typing.Optional[typing.Iterable[global___InterfaceDescriptor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"interfaces",b"interfaces"]) -> None: ...
global___CodecDescriptor = CodecDescriptor

# InterfaceDescriptor describes the implementation of an interface
class InterfaceDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FULLNAME_FIELD_NUMBER: builtins.int
    INTERFACE_ACCEPTING_MESSAGES_FIELD_NUMBER: builtins.int
    INTERFACE_IMPLEMENTERS_FIELD_NUMBER: builtins.int
    # fullname is the name of the interface
    fullname: typing.Text = ...
    # interface_accepting_messages contains information regarding the proto messages which contain the interface as
    # google.protobuf.Any field
    @property
    def interface_accepting_messages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InterfaceAcceptingMessageDescriptor]: ...
    # interface_implementers is a list of the descriptors of the interface implementers
    @property
    def interface_implementers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___InterfaceImplementerDescriptor]: ...
    def __init__(self,
        *,
        fullname : typing.Text = ...,
        interface_accepting_messages : typing.Optional[typing.Iterable[global___InterfaceAcceptingMessageDescriptor]] = ...,
        interface_implementers : typing.Optional[typing.Iterable[global___InterfaceImplementerDescriptor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fullname",b"fullname",u"interface_accepting_messages",b"interface_accepting_messages",u"interface_implementers",b"interface_implementers"]) -> None: ...
global___InterfaceDescriptor = InterfaceDescriptor

# InterfaceImplementerDescriptor describes an interface implementer
class InterfaceImplementerDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FULLNAME_FIELD_NUMBER: builtins.int
    TYPE_URL_FIELD_NUMBER: builtins.int
    # fullname is the protobuf queryable name of the interface implementer
    fullname: typing.Text = ...
    # type_url defines the type URL used when marshalling the type as any
    # this is required so we can provide type safe google.protobuf.Any marshalling and
    # unmarshalling, making sure that we don't accept just 'any' type
    # in our interface fields
    type_url: typing.Text = ...
    def __init__(self,
        *,
        fullname : typing.Text = ...,
        type_url : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fullname",b"fullname",u"type_url",b"type_url"]) -> None: ...
global___InterfaceImplementerDescriptor = InterfaceImplementerDescriptor

# InterfaceAcceptingMessageDescriptor describes a protobuf message which contains
# an interface represented as a google.protobuf.Any
class InterfaceAcceptingMessageDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FULLNAME_FIELD_NUMBER: builtins.int
    FIELD_DESCRIPTOR_NAMES_FIELD_NUMBER: builtins.int
    # fullname is the protobuf fullname of the type containing the interface
    fullname: typing.Text = ...
    # field_descriptor_names is a list of the protobuf name (not fullname) of the field
    # which contains the interface as google.protobuf.Any (the interface is the same, but
    # it can be in multiple fields of the same proto message)
    @property
    def field_descriptor_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]: ...
    def __init__(self,
        *,
        fullname : typing.Text = ...,
        field_descriptor_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"field_descriptor_names",b"field_descriptor_names",u"fullname",b"fullname"]) -> None: ...
global___InterfaceAcceptingMessageDescriptor = InterfaceAcceptingMessageDescriptor

# ConfigurationDescriptor contains metadata information on the sdk.Config
class ConfigurationDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BECH32_ACCOUNT_ADDRESS_PREFIX_FIELD_NUMBER: builtins.int
    # bech32_account_address_prefix is the account address prefix
    bech32_account_address_prefix: typing.Text = ...
    def __init__(self,
        *,
        bech32_account_address_prefix : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"bech32_account_address_prefix",b"bech32_account_address_prefix"]) -> None: ...
global___ConfigurationDescriptor = ConfigurationDescriptor

# MsgDescriptor describes a cosmos-sdk message that can be delivered with a transaction
class MsgDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    MSG_TYPE_URL_FIELD_NUMBER: builtins.int
    # msg_type_url contains the TypeURL of a sdk.Msg.
    msg_type_url: typing.Text = ...
    def __init__(self,
        *,
        msg_type_url : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"msg_type_url",b"msg_type_url"]) -> None: ...
global___MsgDescriptor = MsgDescriptor

# GetAuthnDescriptorRequest is the request used for the GetAuthnDescriptor RPC
class GetAuthnDescriptorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetAuthnDescriptorRequest = GetAuthnDescriptorRequest

# GetAuthnDescriptorResponse is the response returned by the GetAuthnDescriptor RPC
class GetAuthnDescriptorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    AUTHN_FIELD_NUMBER: builtins.int
    # authn describes how to authenticate to the application when sending transactions
    @property
    def authn(self) -> global___AuthnDescriptor: ...
    def __init__(self,
        *,
        authn : typing.Optional[global___AuthnDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"authn",b"authn"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"authn",b"authn"]) -> None: ...
global___GetAuthnDescriptorResponse = GetAuthnDescriptorResponse

# GetChainDescriptorRequest is the request used for the GetChainDescriptor RPC
class GetChainDescriptorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetChainDescriptorRequest = GetChainDescriptorRequest

# GetChainDescriptorResponse is the response returned by the GetChainDescriptor RPC
class GetChainDescriptorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHAIN_FIELD_NUMBER: builtins.int
    # chain describes application chain information
    @property
    def chain(self) -> global___ChainDescriptor: ...
    def __init__(self,
        *,
        chain : typing.Optional[global___ChainDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"chain",b"chain"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"chain",b"chain"]) -> None: ...
global___GetChainDescriptorResponse = GetChainDescriptorResponse

# GetCodecDescriptorRequest is the request used for the GetCodecDescriptor RPC
class GetCodecDescriptorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetCodecDescriptorRequest = GetCodecDescriptorRequest

# GetCodecDescriptorResponse is the response returned by the GetCodecDescriptor RPC
class GetCodecDescriptorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CODEC_FIELD_NUMBER: builtins.int
    # codec describes the application codec such as registered interfaces and implementations
    @property
    def codec(self) -> global___CodecDescriptor: ...
    def __init__(self,
        *,
        codec : typing.Optional[global___CodecDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"codec",b"codec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"codec",b"codec"]) -> None: ...
global___GetCodecDescriptorResponse = GetCodecDescriptorResponse

# GetConfigurationDescriptorRequest is the request used for the GetConfigurationDescriptor RPC
class GetConfigurationDescriptorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetConfigurationDescriptorRequest = GetConfigurationDescriptorRequest

# GetConfigurationDescriptorResponse is the response returned by the GetConfigurationDescriptor RPC
class GetConfigurationDescriptorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONFIG_FIELD_NUMBER: builtins.int
    # config describes the application's sdk.Config
    @property
    def config(self) -> global___ConfigurationDescriptor: ...
    def __init__(self,
        *,
        config : typing.Optional[global___ConfigurationDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"config",b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"config",b"config"]) -> None: ...
global___GetConfigurationDescriptorResponse = GetConfigurationDescriptorResponse

# GetQueryServicesDescriptorRequest is the request used for the GetQueryServicesDescriptor RPC
class GetQueryServicesDescriptorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetQueryServicesDescriptorRequest = GetQueryServicesDescriptorRequest

# GetQueryServicesDescriptorResponse is the response returned by the GetQueryServicesDescriptor RPC
class GetQueryServicesDescriptorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    QUERIES_FIELD_NUMBER: builtins.int
    # queries provides information on the available queryable services
    @property
    def queries(self) -> global___QueryServicesDescriptor: ...
    def __init__(self,
        *,
        queries : typing.Optional[global___QueryServicesDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"queries",b"queries"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"queries",b"queries"]) -> None: ...
global___GetQueryServicesDescriptorResponse = GetQueryServicesDescriptorResponse

# GetTxDescriptorRequest is the request used for the GetTxDescriptor RPC
class GetTxDescriptorRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(self,
        ) -> None: ...
global___GetTxDescriptorRequest = GetTxDescriptorRequest

# GetTxDescriptorResponse is the response returned by the GetTxDescriptor RPC
class GetTxDescriptorResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    TX_FIELD_NUMBER: builtins.int
    # tx provides information on msgs that can be forwarded to the application
    # alongside the accepted transaction protobuf type
    @property
    def tx(self) -> global___TxDescriptor: ...
    def __init__(self,
        *,
        tx : typing.Optional[global___TxDescriptor] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"tx",b"tx"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"tx",b"tx"]) -> None: ...
global___GetTxDescriptorResponse = GetTxDescriptorResponse

# QueryServicesDescriptor contains the list of cosmos-sdk queriable services
class QueryServicesDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    QUERY_SERVICES_FIELD_NUMBER: builtins.int
    # query_services is a list of cosmos-sdk QueryServiceDescriptor
    @property
    def query_services(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QueryServiceDescriptor]: ...
    def __init__(self,
        *,
        query_services : typing.Optional[typing.Iterable[global___QueryServiceDescriptor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"query_services",b"query_services"]) -> None: ...
global___QueryServicesDescriptor = QueryServicesDescriptor

# QueryServiceDescriptor describes a cosmos-sdk queryable service
class QueryServiceDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    FULLNAME_FIELD_NUMBER: builtins.int
    IS_MODULE_FIELD_NUMBER: builtins.int
    METHODS_FIELD_NUMBER: builtins.int
    # fullname is the protobuf fullname of the service descriptor
    fullname: typing.Text = ...
    # is_module describes if this service is actually exposed by an application's module
    is_module: builtins.bool = ...
    # methods provides a list of query service methods
    @property
    def methods(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___QueryMethodDescriptor]: ...
    def __init__(self,
        *,
        fullname : typing.Text = ...,
        is_module : builtins.bool = ...,
        methods : typing.Optional[typing.Iterable[global___QueryMethodDescriptor]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"fullname",b"fullname",u"is_module",b"is_module",u"methods",b"methods"]) -> None: ...
global___QueryServiceDescriptor = QueryServiceDescriptor

# QueryMethodDescriptor describes a queryable method of a query service
# no other info is provided beside method name and tendermint queryable path
# because it would be redundant with the grpc reflection service
class QueryMethodDescriptor(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    FULL_QUERY_PATH_FIELD_NUMBER: builtins.int
    # name is the protobuf name (not fullname) of the method
    name: typing.Text = ...
    # full_query_path is the path that can be used to query
    # this method via tendermint abci.Query
    full_query_path: typing.Text = ...
    def __init__(self,
        *,
        name : typing.Text = ...,
        full_query_path : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"full_query_path",b"full_query_path",u"name",b"name"]) -> None: ...
global___QueryMethodDescriptor = QueryMethodDescriptor
