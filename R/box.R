# AUTO GENERATED FILE - DO NOT EDIT

box <- function(children=NULL, id=NULL, style=NULL, className=NULL, theme=NULL, key=NULL) {
    
    props <- list(children=children, id=id, style=style, className=className, theme=theme, key=key)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'box',
        namespace = 'rimble',
        propNames = c('children', 'id', 'style', 'className', 'theme', 'key'),
        package = 'rimble'
        )

    structure(component, class = c('dash_component', 'list'))
}
