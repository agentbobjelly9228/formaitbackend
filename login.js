import React from 'react'
import { useState } from 'react';
import { revokeAccessToken, OAuthProvider, signInWithCredential, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";
import { useNavigate } from "react-router-dom";


import { auth, getReactNativePersistence, initializeAuth } from '../firebase/firebase'

export default function Login() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    return (
        <div>
            <input placeholder='Email' onChange={(text) => {
                //   console.log(text.target.value)
                setEmail(text.target.value);
            }}></input>
            <input placeholder='Pasword' onChange={(text) => {
                setPassword(text.target.value);
            }}
                type='password'></input>
            <button onClick={() => {
                signInWithEmailAndPassword(auth, email, password).then(() => {
                    console.log("succesfully logged in")
                    navigate("/")
                }).catch((e) => {
                    console.log("wrong password or email")
                })
            }}>Log In</button>
            {/* <button onClick={() => {
            console.log(auth.currentUser.email)
        }}>check logged in</button> */}
        </div>
    )
}
