import { api } from './api';

export default async function addNewPersonService(
  personName: string,
): Promise<void> {
  const data = {
    name: personName,
  };
  const response = await api.post('/persons/', data);
  if (!(response.status === 201)) {
    throw Error('Not possible to create a new person');
  }
}
