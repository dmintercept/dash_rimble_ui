import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'rambda';

import {Box as RBox} from 'rimble-ui';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class box extends Component {
    render() {
        const {children, theme} = this.props;
/*add rbox properties like in qr code
*/
        return (
            <RBox theme={theme}>
                {children}
            </RBox>
        );
    }
}

box.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    
    /**
     * Defines CSS styles which will override styles previously set.
     */
    style: PropTypes.object,
    /**
     * The children of this component
     */
    children: PropTypes.node,
  
    /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,
    
    /**
     * Theme optional
     */
    theme: PropTypes.object,
    /**
     * A unique identifier for the component, used to improve
     * performance by React.js while rendering components
     * See https://reactjs.org/docs/lists-and-keys.html for more info
     */
    key: PropTypes.string,
  };
  