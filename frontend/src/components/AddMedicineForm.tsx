"use client";

import { useState } from "react";

export default function AddMedicineForm() {
  const [name, setName] = useState("");
  const [dosage, setDosage] = useState("");
  const [frequency, setFrequency] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    const newMedicine = { name, dosage, frequency };

    // TODO: Send this to backend API

    console.log("Add medicine:", newMedicine);

    // Clear form after submit
    setName("");
    setDosage("");
    setFrequency("");
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 border rounded">
      <h2 className="text-xl font-semibold mb-4">Add New Medicine</h2>

      <label className="block mb-2">
        Name
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          className="mt-1 block w-full border rounded p-2"
        />
      </label>

      <label className="block mb-2">
        Dosage
        <input
          type="text"
          value={dosage}
          onChange={(e) => setDosage(e.target.value)}
          required
          className="mt-1 block w-full border rounded p-2"
          placeholder="e.g., 500mg"
        />
      </label>

      <label className="block mb-4">
        Frequency
        <input
          type="text"
          value={frequency}
          onChange={(e) => setFrequency(e.target.value)}
          required
          className="mt-1 block w-full border rounded p-2"
          placeholder="e.g., Twice a day"
        />
      </label>

      <button
        type="submit"
        className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition"
      >
        Add Medicine
      </button>
    </form>
  );
}
