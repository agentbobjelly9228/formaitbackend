import React from 'react';
import { useState } from 'react';
import { createUserWithEmailAndPassword } from "firebase/auth";
import { useNavigate } from "react-router-dom";
import { auth } from '../firebase/firebase';

export default function Register() {
    const navigate = useNavigate();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    return (
        <div>
            <div style={{
                width: "400px",
                height: "500px",
                border: "1px solid black",
                borderRadius: "20px",
                position: "absolute",
                left: "calc(50% - 200px)",
                boxShadow: "0 4px 8px 0 rgb(178, 164, 249), 0 6px 20px 0 rgb(178, 164, 249)"
            }}>
                <p style={{
                    fontSize: "40px",
                    textAlign: "center",
                    fontWeight: "bold",
                    color: "rgb(178, 164, 249)"
                }}>Sign In</p>
                <input
                    placeholder='Email'
                    onChange={(e) => setEmail(e.target.value)}
                    style={{
                        width: "250px",
                        position: "absolute",
                        left: "75px",
                        height: "40px"
                    }}
                />
                <input
                    placeholder='Password'
                    type='password'
                    onChange={(e) => setPassword(e.target.value)}
                    style={{
                        width: "250px",
                        position: "absolute",
                        left: "75px",
                        top: "200px",
                        height: "40px"
                    }}
                />
                <button
                    style={{
                        width: "250px",
                        position: "absolute",
                        left: "75px",
                        top: "270px",
                        height: "40px",
                        borderRadius: "20px",
                        borderWidth: "1px",
                        backgroundColor: "rgb(178, 164, 249)"
                    }}
                    onClick={() => {
                        createUserWithEmailAndPassword(auth, email, password)
                            .then(() => {
                                console.log("successfully registered");
                                navigate("/");
                            })
                            .catch((e) => {
                                console.log("email already in use!");
                            });
                    }}>Register</button>
            </div>
        </div>
    );
}
