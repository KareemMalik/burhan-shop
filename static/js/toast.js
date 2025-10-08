function showToast(title, message, type = 'normal', duration = 3000) {
  const el = document.getElementById('toast-component');
  if (!el) return;

  // Reset base glass style
  el.className =
    'fixed bottom-8 right-8 flex items-center gap-4 px-6 py-4 rounded-2xl shadow-2xl border backdrop-blur-md z-50 transition-all duration-300 translate-y-64 opacity-0';

  // Warna sesuai tipe
  if (type === 'success') {
    el.classList.add('bg-emerald-500/30', 'border-emerald-400/50', 'text-white');
    document.getElementById('toast-icon').textContent = '✅';
  } else if (type === 'error') {
    el.classList.add('bg-red-500/30', 'border-red-400/50', 'text-white');
    document.getElementById('toast-icon').textContent = '⚠️';
  } else if (type === 'info') {
    el.classList.add('bg-blue-500/30', 'border-blue-400/50', 'text-white');
    document.getElementById('toast-icon').textContent = 'ℹ️';
  } else {
    el.classList.add('bg-white/10', 'border-white/20', 'text-white');
    document.getElementById('toast-icon').textContent = '💬';
  }

  // Isi teks
  document.getElementById('toast-title').textContent = title;
  document.getElementById('toast-message').textContent = message;

  // Tampilkan animasi
  el.classList.remove('opacity-0', 'translate-y-64');
  el.classList.add('opacity-100', 'translate-y-0');

  // Hilangkan setelah durasi
  setTimeout(() => {
    el.classList.remove('opacity-100', 'translate-y-0');
    el.classList.add('opacity-0', 'translate-y-64');
  }, duration);
}
