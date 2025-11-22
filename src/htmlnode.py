class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list | None = None,
        props: dict[str, str] | None = None,
    ):

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Will be used by child classes"""
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        """Returns a formatted string representing the HTML attributes of the node"""
        if self.props == None or self.props == {}:
            return ""
        prop_string = ""
        for pair in self.props:
            prop_string += f' {pair}="{self.props[pair]}"'
        return prop_string

    def __repr__(self):
        return f"HTMLNode: {self.tag}, {self.value}, children: {self.children}, {self.props}"

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict | None = None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        """Function for formatting text"""
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def __eq__(self, other):
        return super().__eq__(other)


class ParentNode(HTMLNode):
    def __init__(
            #wanted to have list[HTMLNode] v here but causes an error]
        self, tag: str | None, children: list | None, props: dict | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        """Function for formatting stored child (leaf) nodes"""
        if self.tag == None:
            raise ValueError("All parent nodes must have a tag for proper formatting")
        if self.children == None:
            raise ValueError("All parent nodes must have children")
        leaf_nodes = ""
        for node in self.children:
            leaf_nodes += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{leaf_nodes}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def __eq__(self, other):
        return super().__eq__(other)
