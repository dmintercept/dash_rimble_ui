# AUTO GENERATED FILE - DO NOT EDIT

qr <- function(id=NULL, className=NULL, key=NULL, value=NULL) {
    
    props <- list(id=id, className=className, key=key, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'qr',
        namespace = 'rimble',
        propNames = c('id', 'className', 'key', 'value'),
        package = 'rimble'
        )

    structure(component, class = c('dash_component', 'list'))
}
