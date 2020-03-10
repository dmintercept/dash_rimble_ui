# AUTO GENERATED FILE - DO NOT EDIT

metamask <- function(id=NULL, value=NULL, borderRadius=NULL, boxShadow=NULL, width=NULL, className=NULL, key=NULL) {
    
    props <- list(id=id, value=value, borderRadius=borderRadius, boxShadow=boxShadow, width=width, className=className, key=key)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'metamask',
        namespace = 'rimble',
        propNames = c('id', 'value', 'borderRadius', 'boxShadow', 'width', 'className', 'key'),
        package = 'rimble'
        )

    structure(component, class = c('dash_component', 'list'))
}
