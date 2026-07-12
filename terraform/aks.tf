resource "azurerm_kubernetes_cluster" "aks" {
  name                = var.aks_name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  dns_prefix          = "hostingreliability"

  default_node_pool {
    name    = "system"
    vm_size = var.aks_vm_size

    auto_scaling_enabled = true
    min_count            = 1
    max_count            = 2
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Project     = "HostingReliabilityPlatform"
    Environment = "Development"
    Owner       = "Imtiyaz"
  }
}