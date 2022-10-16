import React, { useEffect, useState } from 'react';
import { InputNewPerson } from '../components/InputNewPerson';
import {
  getAllPersonsService,
  Person,
} from '../services/get-all-persons-serivce';

export function Dashboard() {
  const [persons, setPersons] = useState<Person[]>([]);

  useEffect(() => {
    const allPersons = async () => {
      const response = await getAllPersonsService();
      setPersons(response);
    };

    allPersons();
  }, []);
  return (
    <>
      <InputNewPerson />
      <h3>Todas as Pessoas </h3>
      <ul>
        {persons.map((e: Person) => (
          <li key={e.name}>{e.name}</li>
        ))}
      </ul>
    </>
  );
}
