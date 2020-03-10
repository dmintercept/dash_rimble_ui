# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class metamask(Component):
    """A metamask component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- id (string; optional): The ID of this component, used to identify dash components
in callbacks. The ID needs to be unique across all of the
components in an app.
- value (string; optional)
- borderRadius (number; optional): Defines CSS styles which will override styles previously set.
- boxShadow (number; optional): The children of this component
- width (number; optional): Often used with CSS to style elements with common properties.
- className (string; optional): Often used with CSS to style elements with common properties.
- key (string; optional): A unique identifier for the component, used to improve
performance by React.js while rendering components
See https://reactjs.org/docs/lists-and-keys.html for more info"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, value=Component.UNDEFINED, borderRadius=Component.UNDEFINED, boxShadow=Component.UNDEFINED, width=Component.UNDEFINED, className=Component.UNDEFINED, key=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'value', 'borderRadius', 'boxShadow', 'width', 'className', 'key']
        self._type = 'metamask'
        self._namespace = 'rimble'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'value', 'borderRadius', 'boxShadow', 'width', 'className', 'key']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(metamask, self).__init__(**args)
