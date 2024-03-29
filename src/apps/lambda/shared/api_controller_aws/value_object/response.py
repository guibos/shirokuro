import dataclasses

from apps.aws.shared.api_controller_aws.value_object.body import Body
from apps.aws.shared.api_controller_aws.value_object.status_code import StatusCode


@dataclasses.dataclass
class Response:
    status_code: StatusCode
    body: Body
