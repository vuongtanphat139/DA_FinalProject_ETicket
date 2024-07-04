import { Helmet } from 'react-helmet-async';
// ----------------------------------------------------------------------

export default function UserPage() {
  return (
    <>
      <Helmet>
        <title> User | Minimal UI </title>
      </Helmet>

      <table className="table table-striped-columns">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
          </tr>
        </thead>
        <tbody>
          <tr className='flex text-center items-center justify-center content-center self-center object-center center'>
            <th style={{ textAlign: "center"}} scope="row">1</th>
            <td style={{ textAlign: "center"}}>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Thornton</td>
            <td>@twitter</td>
          </tr>
        </tbody>
      </table>
    </>
  );
}
