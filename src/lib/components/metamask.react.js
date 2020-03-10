import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'rambda';

import {MetaMaskButton as MB} from 'rimble-ui';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class metamask extends Component {
    render() {
        const {id,borderRadius, boxShadow, width, value, ...otherProps} = this.props;
/*add rbox properties like in qr code
*/
        return (
            <MB id={id} borderRadius={borderRadius} boxShadow={boxShadow} width={width}>
                {value}
            </MB>
        );
    }
}

metamask.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    /*
    *text
    */
   value: PropTypes.string,
    /**
     * Defines CSS styles which will override styles previously set.
     */
    borderRadius: PropTypes.number,
    /**
     * The children of this component
     */
    boxShadow: PropTypes.number,
  
    /**
     * Often used with CSS to style elements with common properties.
     */
    width: PropTypes.number,
     /**
     * Often used with CSS to style elements with common properties.
     */
    className: PropTypes.string,

    /**
     * A unique identifier for the component, used to improve
     * performance by React.js while rendering components
     * See https://reactjs.org/docs/lists-and-keys.html for more info
     */
    key: PropTypes.string,
  };
  