write_file src/pages/CustomerDetails.tsx <<'EOF'
import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'
import { fetchAPI } from '../utils/api'

export default function CustomerDetails() {
  const { id } = useParams()
  const [customer, setCustomer] = useState(null)

  useEffect(() => {
    fetchAPI(`/customers/${id}`).then(setCustomer)
  }, [id])

  if (!customer) return <p className="text-silver">Loading…</p>

  return (
    <div>
      <h1 className="text-2xl font-display text-gold mb-4">{customer.name}</h1>
      <div className="glass-card p-6 rounded-xl">
        <p className="text-silver">Email: {customer.email}</p>
        <p className="text-silver mt-2">Phone: {customer.phone || 'N/A'}</p>
        <p className="text-silver mt-2">Orders: {customer.orderCount}</p>
        <p className="text-silver mt-2">Total spent: ${customer.totalSpent}</p>
        <p className="text-silver mt-2">Trust score: {customer.trustScore}</p>
      </div>
    </div>
  )
}
EOF