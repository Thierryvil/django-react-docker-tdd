import React, { useState } from 'react';
import { makeStyles, TextField, Button } from '@material-ui/core';
import { obtainAuthTokenService } from '../services/obtain-auth-token-service';

const useStyles = makeStyles({
  root: {
    margin: 'auto',
    padding: '10px',
    display: 'flex',
    flexDirection: 'column',
    width: '50%',
    flexWrap: 'wrap',
    justifyContent: 'center',
  },
});

export function Login() {
  const classes = useStyles();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    const response = await obtainAuthTokenService({ username, password });
    localStorage.setItem('access_token', response.data.acesss);
  };

  return (
    <form className={classes.root} onSubmit={handleLogin}>
      <TextField
        id="standard-basic"
        label="Username"
        variant="standard"
        onChange={(e) => setUsername(e.target.value)}
      />
      <TextField
        id="standard-basic"
        label="Password"
        variant="standard"
        onChange={(e) => setPassword(e.target.value)}
      />
      <Button type="submit" variant="contained">
        Login
      </Button>
    </form>
  );
}
