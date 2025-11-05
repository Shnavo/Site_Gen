class HTMLNode():
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list | None = None, 
        props: dict | None = None
    ):
        
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        '''Will be used by child classes'''
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self) -> str:
        '''Returns a formatted string representing the HTML attributes of the node'''
        if self.props == None or self.props == {}:
            return ""
        prop_string = ""
        for pair in self.props:
            prop_string += f' {pair}="{self.props[pair]}"'
        return prop_string

    def __repr__(self):
        return f'HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}'
    
    def __eq__(self, other):
        return (
            self.tag == other.tag 
            and self.value == other.value 
            and self.children == other.children
            and self.props == other.props
        )
