# AUTO GENERATED FILE - DO NOT EDIT

ethaddress <- function(id=NULL, address=NULL, textLabels=NULL, key=NULL) {
    
    props <- list(id=id, address=address, textLabels=textLabels, key=key)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ethaddress',
        namespace = 'rimble',
        propNames = c('id', 'address', 'textLabels', 'key'),
        package = 'rimble'
        )

    structure(component, class = c('dash_component', 'list'))
}
