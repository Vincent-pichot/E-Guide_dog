import React from 'react';

function DisplayUrl(props) {
    return (
        <>
            <iframe title='frame-website' src={props.url} width="100%" height="700" />
        </>
    )
}

export default DisplayUrl;