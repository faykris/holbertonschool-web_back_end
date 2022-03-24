import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";
import {validateUseBuiltInsOption} from "@babel/preset-env/lib/normalize-options";

export default function handleProfileSignup(firstname, lastname, filename) {
    return Promise.all(
        [signUpUser(firstname, lastname), uploadPhoto(filename)]
    ).then((res, err) => {

    });
}
