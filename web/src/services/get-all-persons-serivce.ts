import { api } from './api';

export interface Person {
  name: string;
}

export async function getAllPersonsService(): Promise<Person[]> {
  const response = await api.get('/persons/');
  if (!(response.status === 200)) {
    throw Error('Problems to get all persons');
  }

  return response.data;
}
