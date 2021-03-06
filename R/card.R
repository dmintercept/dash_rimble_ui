# AUTO GENERATED FILE - DO NOT EDIT

card <- function(children=NULL, id=NULL, style=NULL, className=NULL, key=NULL, color=NULL, body=NULL, outline=NULL, inverse=NULL, loading_state=NULL) {
    
    props <- list(children=children, id=id, style=style, className=className, key=key, color=color, body=body, outline=outline, inverse=inverse, loading_state=loading_state)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'card',
        namespace = 'rimble',
        propNames = c('children', 'id', 'style', 'className', 'key', 'color', 'body', 'outline', 'inverse', 'loading_state'),
        package = 'rimble'
        )

    structure(component, class = c('dash_component', 'list'))
}
