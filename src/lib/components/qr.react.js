import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'rambda';

import {QR as R_QR} from 'rimble-ui';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class qr extends Component {
    render() {
        /*This is deconstructing the list into lists of properties
        */
        const {id, value, ...otherProps} = this.props;

        return (
            <R_QR id = {id} value = {value}>

            </R_QR>
        );
    }
}

qr.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
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
  
    /**
     * value of qr code
     */
    value: PropTypes.string,
    
  };
  