import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useSearch } from './SearchContext';

const Search = () => {
  const [searchTerm, setSearchTerm] = useState(''); // State to manage search term
  const { setSearchQuery } = useSearch(); // If using context to manage search globally

  const navigate = useNavigate();

  const handleSubmit = () => {
    event.preventDefault(); // Prevent the default form submission
    setSearchQuery(searchTerm); // Example if using context
    navigate('/events');
  };

  const handleInputChange = (event) => {
    setSearchTerm(event.target.value); // Update search term as user types
  };

  return (
    <form className="flex justify-start max-w-3xl mx-auto" onSubmit={handleSubmit}>
      <label htmlFor="simple-search" className="sr-only">
        Search
      </label>
      <div className="relative w-full">
        <input
          type="text"
          id="simple-search"
          className="bg-[#100000] border border-gray-300 text-white text-sm focus:ring-primary-500 focus:border-primary-500 block w-full p-2.5 "
          placeholder="Search events, concerts, workshops..."
          onChange={handleInputChange} // Handle input change
        />
      </div>
      <button
        type="submit"
        className="p-2.5 ms-2 text-sm font-medium text-white bg-primary-500 border border-primary-500 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300"
      >
        <svg
          className="w-4 h-4"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 20 20"
        >
          <path
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="m19 19-4-4m0-7A7 7 0 1 1 1 8a7 7 0 0 1 14 0Z"
          />
        </svg>
        {/* <span className="sr-only">Search</span> */}
      </button>
    </form>
  );
};

export default Search;
