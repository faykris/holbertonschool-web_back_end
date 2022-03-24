export default function handleResponseFromAPI(promise) {
    return new Promise((resolve, reject) => {
        if (promise instanceof Promise) {
            resolve({
                status: 200,
                body: 'Success',
            });
        }
        else {
            reject();
        }
    }).then(res => {
        console.log("Got a response from the API");
    }).catch(err => {
        console.log("Got a response from the API");
    });
}
