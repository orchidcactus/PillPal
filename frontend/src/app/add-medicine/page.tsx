import AddMedicineForm from "@/components/AddMedicineForm";

export default function AddMedicinePage() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-4">Add New Medicine</h1>
      <AddMedicineForm />
    </main>
  );
}
