# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import ticket_management_pb2 as ticket__management__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in ticket_management_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class TicketServiceStub(object):
    """Service để quản lý vé
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTicket = channel.unary_unary(
                '/TicketService/AddTicket',
                request_serializer=ticket__management__pb2.TicketRequest.SerializeToString,
                response_deserializer=ticket__management__pb2.TicketResponse.FromString,
                _registered_method=True)
        self.UpdateTicket = channel.unary_unary(
                '/TicketService/UpdateTicket',
                request_serializer=ticket__management__pb2.Ticket.SerializeToString,
                response_deserializer=ticket__management__pb2.TicketResponse.FromString,
                _registered_method=True)
        self.GetAllTickets = channel.unary_unary(
                '/TicketService/GetAllTickets',
                request_serializer=ticket__management__pb2.GetAllTicketsRequest.SerializeToString,
                response_deserializer=ticket__management__pb2.GetAllTicketsResponse.FromString,
                _registered_method=True)
        self.DeleteTicket = channel.unary_unary(
                '/TicketService/DeleteTicket',
                request_serializer=ticket__management__pb2.DeleteTicketRequest.SerializeToString,
                response_deserializer=ticket__management__pb2.DeleteTicketResponse.FromString,
                _registered_method=True)


class TicketServiceServicer(object):
    """Service để quản lý vé
    """

    def AddTicket(self, request, context):
        """RPC để thêm một vé
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTicket(self, request, context):
        """RPC để cập nhật một vé
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTickets(self, request, context):
        """RPC để lấy tất cả vé
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTicket(self, request, context):
        """RPC để xóa một vé
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TicketServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTicket': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTicket,
                    request_deserializer=ticket__management__pb2.TicketRequest.FromString,
                    response_serializer=ticket__management__pb2.TicketResponse.SerializeToString,
            ),
            'UpdateTicket': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTicket,
                    request_deserializer=ticket__management__pb2.Ticket.FromString,
                    response_serializer=ticket__management__pb2.TicketResponse.SerializeToString,
            ),
            'GetAllTickets': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTickets,
                    request_deserializer=ticket__management__pb2.GetAllTicketsRequest.FromString,
                    response_serializer=ticket__management__pb2.GetAllTicketsResponse.SerializeToString,
            ),
            'DeleteTicket': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTicket,
                    request_deserializer=ticket__management__pb2.DeleteTicketRequest.FromString,
                    response_serializer=ticket__management__pb2.DeleteTicketResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TicketService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('TicketService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TicketService(object):
    """Service để quản lý vé
    """

    @staticmethod
    def AddTicket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TicketService/AddTicket',
            ticket__management__pb2.TicketRequest.SerializeToString,
            ticket__management__pb2.TicketResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTicket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TicketService/UpdateTicket',
            ticket__management__pb2.Ticket.SerializeToString,
            ticket__management__pb2.TicketResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllTickets(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TicketService/GetAllTickets',
            ticket__management__pb2.GetAllTicketsRequest.SerializeToString,
            ticket__management__pb2.GetAllTicketsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTicket(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/TicketService/DeleteTicket',
            ticket__management__pb2.DeleteTicketRequest.SerializeToString,
            ticket__management__pb2.DeleteTicketResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
<<<<<<< HEAD
=======


class OrderServiceStub(object):
    """Service để quản lý đơn hàng
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddOrder = channel.unary_unary(
                '/OrderService/AddOrder',
                request_serializer=ticket__management__pb2.OrderRequest.SerializeToString,
                response_deserializer=ticket__management__pb2.OrderResponse.FromString,
                _registered_method=True)
        self.UpdateOrder = channel.unary_unary(
                '/OrderService/UpdateOrder',
                request_serializer=ticket__management__pb2.Order.SerializeToString,
                response_deserializer=ticket__management__pb2.OrderResponse.FromString,
                _registered_method=True)
        self.GetAllOrders = channel.unary_unary(
                '/OrderService/GetAllOrders',
                request_serializer=ticket__management__pb2.GetAllOrdersRequest.SerializeToString,
                response_deserializer=ticket__management__pb2.GetAllOrdersResponse.FromString,
                _registered_method=True)
        self.DeleteOrder = channel.unary_unary(
                '/OrderService/DeleteOrder',
                request_serializer=ticket__management__pb2.DeleteOrderRequest.SerializeToString,
                response_deserializer=ticket__management__pb2.DeleteOrderResponse.FromString,
                _registered_method=True)


class OrderServiceServicer(object):
    """Service để quản lý đơn hàng
    """

    def AddOrder(self, request, context):
        """RPC để thêm một đơn hàng
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateOrder(self, request, context):
        """RPC để cập nhật một đơn hàng
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllOrders(self, request, context):
        """RPC để lấy tất cả đơn hàng
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOrder(self, request, context):
        """RPC để xóa một đơn hàng
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.AddOrder,
                    request_deserializer=ticket__management__pb2.OrderRequest.FromString,
                    response_serializer=ticket__management__pb2.OrderResponse.SerializeToString,
            ),
            'UpdateOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateOrder,
                    request_deserializer=ticket__management__pb2.Order.FromString,
                    response_serializer=ticket__management__pb2.OrderResponse.SerializeToString,
            ),
            'GetAllOrders': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllOrders,
                    request_deserializer=ticket__management__pb2.GetAllOrdersRequest.FromString,
                    response_serializer=ticket__management__pb2.GetAllOrdersResponse.SerializeToString,
            ),
            'DeleteOrder': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOrder,
                    request_deserializer=ticket__management__pb2.DeleteOrderRequest.FromString,
                    response_serializer=ticket__management__pb2.DeleteOrderResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'OrderService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('OrderService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OrderService(object):
    """Service để quản lý đơn hàng
    """

    @staticmethod
    def AddOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/OrderService/AddOrder',
            ticket__management__pb2.OrderRequest.SerializeToString,
            ticket__management__pb2.OrderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/OrderService/UpdateOrder',
            ticket__management__pb2.Order.SerializeToString,
            ticket__management__pb2.OrderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllOrders(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/OrderService/GetAllOrders',
            ticket__management__pb2.GetAllOrdersRequest.SerializeToString,
            ticket__management__pb2.GetAllOrdersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/OrderService/DeleteOrder',
            ticket__management__pb2.DeleteOrderRequest.SerializeToString,
            ticket__management__pb2.DeleteOrderResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
>>>>>>> origin/ticket_management3
