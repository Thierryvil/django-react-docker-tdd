import { api } from './api';

interface AuthProps {
  username: string;
  password: string;
}

export async function obtainAuthTokenService(props: AuthProps) {
  const response = await api.post('/auth/token/', props);
  if (!(response.status === 200)) {
    throw Error('Invalid Credentials');
  }
  return response;
}
