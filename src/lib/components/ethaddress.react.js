import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {omit} from 'rambda';

import {EthAddress as REthAddress} from 'rimble-ui';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class address extends Component {
    render() {
        const {address, textLabels} = this.props;
/*add rbox properties like in qr code
*/
        return (
            <REthAddress address={address} textLabels={textLabels}>
                
            </REthAddress>
        );
    }
}

address.propTypes = {
    /**
     * The ID of this component, used to identify dash components
     * in callbacks. The ID needs to be unique across all of the
     * components in an app.
     */
    id: PropTypes.string,
    
    /**
     * Eth Address.
     */
    address: PropTypes.string,
    /**
     * The children of this component
     */
    textLabels: PropTypes.bool,
  
    /**
     * A unique identifier for the component, used to improve
     * performance by React.js while rendering components
     * See https://reactjs.org/docs/lists-and-keys.html for more info
     */
    key: PropTypes.string,
  };
  