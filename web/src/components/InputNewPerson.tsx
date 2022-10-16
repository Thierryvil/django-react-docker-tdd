import React, { useState } from 'react';
import {
  Box,
  Button,
  CardActions,
  CardContent,
  TextField,
} from '@material-ui/core';
import addNewPersonService from '../services/add-new-person-service';

export function InputNewPerson() {
  const [personName, setPersonName] = useState('');

  const handleClick = async () => {
    try {
      await addNewPersonService(personName);
    } catch (error) {}
  };
  return (
    <Box sx={{ minWidth: 275 }}>
      <CardContent>
        <TextField
          id="outlined-basic"
          label="Nome da Pessoa"
          variant="outlined"
          onChange={(event) => setPersonName(event.target.value)}
        />
        <CardActions>
          <Button color="primary" onClick={() => handleClick()}>
            Add
          </Button>
        </CardActions>
      </CardContent>
    </Box>
  );
}
