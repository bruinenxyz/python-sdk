from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="GoogleThreadInput")


@attr.s(auto_attribs=True)
class GoogleThreadInput:
    """The input for your google thread

    Attributes:
        thread_id (str): The id of the thread
    """

    thread_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        thread_id = self.thread_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "threadId": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        thread_id = d.pop("threadId")

        google_thread_input = cls(
            thread_id=thread_id,
        )

        google_thread_input.additional_properties = d
        return google_thread_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
